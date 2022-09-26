from math import ceil

from odoo import fields, models


class ProjectTask(models.Model):

    _inherit = "project.task"

    timesheet_suggested_message = fields.Char(
        "Suggested timesheet message",
        compute="_compute_timesheet_suggested_message",
        help="Task display name timesheet message as suggestion",
    )
    timesheet_suggested_duration = fields.Float(
        "Suggested timesheet duration",
        compute="_compute_timesheet_suggested_duration",
        help="Suggested time for a timesheet record based on stage changes",
    )

    def _compute_timesheet_suggested_message(self):
        """
        Compute suggested message to timesheet record
        """
        for rec in self:
            partner_name = rec.commercial_partner_id.name or ""
            msg = "{}, {}: ".format(rec.display_name, partner_name)
            rec.timesheet_suggested_message = msg

    def _compute_timesheet_suggested_duration(self):
        """
        Compute suggested time to timesheet record
        """
        for rec in self:
            # The latest message is usually the "stage changed"-message.
            # We'll calculate the suggested duration from that

            # Default to minimum duration
            minutes_spent = int(
                self.env["ir.config_parameter"]
                .sudo()
                .get_param("hr_timesheet.timesheet_min_duration", 0)
            )
            if rec.message_ids:
                # Elapsed time in minutes
                minutes_spent = (
                    fields.datetime.now() - rec.message_ids[0].date
                ).seconds / 60

            rounding = int(
                self.env["ir.config_parameter"]
                .sudo()
                .get_param("hr_timesheet.timesheet_rounding", 0)
            )

            if rounding and ceil(minutes_spent % rounding) != 0:
                minutes_spent = ceil(minutes_spent / rounding) * rounding

            rec.timesheet_suggested_duration = minutes_spent / 60
