import logging

import pytz

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class AccountAnalyticLine(models.Model):
    _inherit = "account.analytic.line"

    def _user_tz_name(self, user):
        """Return user's timezone name or UTC fallback."""
        tzname = (user.tz or "UTC").strip() or "UTC"
        try:
            pytz.timezone(tzname)
            return tzname
        except Exception:
            return "UTC"

    def _utcnow_aware(self):
        """Return current UTC time (timezone-aware)."""
        now = fields.Datetime.now()
        if now.tzinfo is None:
            return pytz.UTC.localize(now)
        return now.astimezone(pytz.UTC)

    def _to_utc_aware(self, dt):
        """Convert datetime to UTC timezone-aware format."""
        if dt is None:
            return None
        if dt.tzinfo is None:
            return pytz.UTC.localize(dt)
        return dt.astimezone(pytz.UTC)

    def _get_calendar_cutoff(self, employee):
        """Return cutoff configuration from resource calendar (employee or company)."""
        calendar = None
        if employee and getattr(employee, "resource_calendar_id", False):
            calendar = employee.resource_calendar_id
        if not calendar:
            calendar = self.env.company.resource_calendar_id

        return {
            "enabled": bool(getattr(calendar, "ts_cutoff_enabled", False)),
            "hour": int(getattr(calendar, "ts_cutoff_hour", 18) or 18),
            "minute": int(getattr(calendar, "ts_cutoff_minute", 0) or 0),
            "block_start": bool(getattr(calendar, "ts_block_start_after_cutoff", False)),
        }

    def _get_emp_cutoff(self, employee):
        """
        Return employee-specific cutoff if
        override enabled, else calendar configuration.
        """
        conf = self._get_calendar_cutoff(employee)
        if employee and getattr(employee, "ts_cutoff_override", False):
            conf.update(
                {
                    "enabled": bool(
                        getattr(employee, "ts_cutoff_enabled_emp", conf["enabled"])
                    ),
                    "hour": int(
                        getattr(employee, "ts_cutoff_hour_emp", conf["hour"])
                        or conf["hour"]
                    ),
                    "minute": int(
                        getattr(employee, "ts_cutoff_minute_emp", conf["minute"])
                        or conf["minute"]
                    ),
                    "block_start": bool(
                        getattr(
                            employee,
                            "ts_block_start_after_cutoff_emp",
                            conf["block_start"],
                        )
                    ),
                }
            )
        return conf

    def _today_cutoff_utc(self, user, employee):
        """Calculate today's cutoff time in UTC for the user's local timezone."""
        conf = self._get_emp_cutoff(employee)
        tzname = self._user_tz_name(user)
        tz = pytz.timezone(tzname)
        now_local = fields.Datetime.context_timestamp(
            self.with_context(tz=tzname), fields.Datetime.now()
        )
        if now_local.tzinfo is None:
            now_local = tz.localize(now_local)

        cutoff_local = now_local.replace(
            hour=conf["hour"], minute=conf["minute"], second=0, microsecond=0
        )
        if cutoff_local.tzinfo is None:
            cutoff_local = tz.localize(cutoff_local)
        return cutoff_local.astimezone(pytz.UTC), conf

    @api.model
    def _auto_stop_running_at_cutoff(self, batch=2000):
        """Cron: automatically stop running timesheets at cutoff time."""
        try:
            HourUom = self.env.ref("uom.product_uom_hour")
            hour_uom_id = HourUom.id
        except Exception:
            return True

        domain = [
            ("date_time", "!=", False),
            ("project_id.allow_timesheets", "=", True),
            ("unit_amount", "=", 0),
            ("product_uom_id", "=", hour_uom_id),
        ]
        lines = self.sudo().search(domain, limit=batch)
        if not lines:
            return True

        now_utc = self._utcnow_aware()
        processed = 0

        for line in lines:
            user = line.user_id or self.env.user
            employee = line.employee_id or getattr(user, "employee_id", False)
            cutoff_utc, conf = self._today_cutoff_utc(user, employee)

            if not conf.get("enabled") or now_utc < cutoff_utc or not line.date_time:
                continue

            start_dt_utc = self._to_utc_aware(
                fields.Datetime.to_datetime(line.date_time)
            )
            if start_dt_utc >= cutoff_utc:
                continue

            duration_hours = (cutoff_utc - start_dt_utc).total_seconds() / 3600.0
            new_amount = max(0.0, duration_hours)

            try:
                line.unit_amount = new_amount
                processed += 1
            except Exception:
                continue

        return True
