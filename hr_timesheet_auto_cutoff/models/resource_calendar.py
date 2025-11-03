# -*- coding: utf-8 -*-
import logging

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class ResourceCalendar(models.Model):
    _inherit = "resource.calendar"

    # Cutoff-asetukset ovat nyt kalenterilla
    ts_cutoff_enabled = fields.Boolean(
        string="Enable timesheet cutoff",
        help="If enabled, running timers will be auto-stopped at cutoff time."
    )
    ts_cutoff_hour = fields.Integer(
        string="Cutoff hour (0–23)",
        default=18,
        help="Hour of day in the calendar's timezone when timers are cut off."
    )
    ts_cutoff_minute = fields.Integer(
        string="Cutoff minute (0–59)",
        default=0,
        help="Minute of hour when timers are cut off."
    )
    ts_block_start_after_cutoff = fields.Boolean(
        string="Block starting a timer after cutoff",
        help="If enabled, users cannot start a new timer after the cutoff."
    )

    @api.constrains("ts_cutoff_hour", "ts_cutoff_minute")
    def _check_cutoff_bounds(self):
        for cal in self:
            if cal.ts_cutoff_hour is not None and not (0 <= int(cal.ts_cutoff_hour) <= 23):
                raise ValidationError(_("Cutoff hour must be between 0 and 23."))
            if cal.ts_cutoff_minute is not None and not (0 <= int(cal.ts_cutoff_minute) <= 59):
                raise ValidationError(_("Cutoff minute must be between 0 and 59."))
