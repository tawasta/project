from odoo import fields, models


class ProjectTask(models.Model):

    _inherit = "project.task"

    resolution_time = fields.Float(
        string="Resolution time", compute="_compute_resolution_time", store=True
    )

    number_of_responses = fields.Integer(
        string="Number of responses", compute="_compute_msg_count", store=True
    )

    def _compute_resolution_time(self):
        for record in self:
            if record.date_assign and record.stage_id.name == "Done":
                # Lasketaan aika taskin luomisen ja donen välillä eli luomisesta
                # siihen hetkeen, kun tila muuttui doneksi
                delta = record.date_last_stage_update - record.date_assign
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
