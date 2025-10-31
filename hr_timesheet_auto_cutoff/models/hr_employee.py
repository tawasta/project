from odoo import fields, models


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    ts_cutoff_override = fields.Boolean(string="Override global cutoff")
    ts_cutoff_enabled_emp = fields.Boolean(string="Enable cutoff for this employee")
    ts_cutoff_hour_emp = fields.Integer(string="Cutoff hour (0–23)")
    ts_cutoff_minute_emp = fields.Integer(string="Cutoff minute (0–59)")
    ts_block_start_after_cutoff_emp = fields.Boolean(
        string="Block starting a timer after cutoff"
    )

    def _check_bounds(self, val, low, high, fallback):
        """Ensure value is within numeric bounds, fallback if invalid."""
        try:
            i = int(val)
        except Exception:
            return fallback
        return i if low <= i <= high else fallback

    def write(self, vals):
        """Validate numeric cutoff values before saving."""
        if "ts_cutoff_hour_emp" in vals:
            vals["ts_cutoff_hour_emp"] = self._check_bounds(
                vals["ts_cutoff_hour_emp"], 0, 23, 18
            )
        if "ts_cutoff_minute_emp" in vals:
            vals["ts_cutoff_minute_emp"] = self._check_bounds(
                vals["ts_cutoff_minute_emp"], 0, 59, 0
            )
        return super().write(vals)
