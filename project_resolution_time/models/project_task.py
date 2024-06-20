import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class ProjectTask(models.Model):

    _inherit = "project.task"

    resolution_time = fields.Float(
        string="Resolution Time (h)",
        compute="_compute_resolution_time",
        store=True,
        default=None,
        help="Time in hours from the creation of the task to its last moving "
        "to a closed stage",
    )

    number_of_responses = fields.Integer(
        string="Number of responses", compute="_compute_msg_count", store=True
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

    def _compute_msg_count(self):
        for record in self:
            count = 0
            if record.website_message_ids:
                for message in record.message_ids:
                    if message.message_type == "comment":
                        count += 1
            record.number_of_responses = count
