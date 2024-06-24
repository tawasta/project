import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class ProjectTask(models.Model):

    _inherit = "project.task"

    resolution_time = fields.Float(
        string="Resolution Time (days)",
        compute="_compute_resolution_time",
        store=True,
        default=None,
        help="Time in days from the creation of the task to its last moving "
        "to a closed stage",
    )

    @api.depends("stage_id")
    def _compute_resolution_time(self):
        for record in self:
            if (
                record.create_date
                and record.date_last_stage_update
                and record.stage_id.is_closed
            ):
                # Time between create date and resolving date
                delta = record.date_last_stage_update - record.create_date
                delay_days = delta.days + delta.seconds / (24 * 3600)
                record.resolution_time = delay_days
            else:
                record.resolution_time = False
