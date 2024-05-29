from odoo import api, fields, models


class ProjectTask(models.Model):

    _inherit = "project.task"

    resolution_time = fields.Float(
        string="Resolution time",
        compute="_compute_resolution_time",
        store=True,
        default=None,
    )

    number_of_responses = fields.Integer(
        string="Number of responses", compute="_compute_msg_count", store=True
    )

    @api.depends("stage_id")
    def _compute_resolution_time(self):
        # Tänne create date
        for record in self:
            if record.create_date and record.stage_id.name == "Done":
                # Time between create date and resolvng date
                delta = record.date_last_stage_update - self.create_date
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
