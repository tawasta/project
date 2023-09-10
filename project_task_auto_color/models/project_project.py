from odoo import fields, models


class Project(models.Model):

    _inherit = "project.project"

    def action_compute_task_colors(self):
        for record in self:
            record._compute_task_colors()

    def _compute_task_colors(self):
        self.ensure_one()
        for task in self.task_ids:
            if not task.message_ids:
                # There shouldn't really be any cases where task has no messages,
                # but check it just in case
                continue
            latest_message = task.message_ids[0]
            latest_message_age = fields.Datetime.now() - latest_message.date
            latest_message_age_days = latest_message_age.days

            if latest_message_age_days <= 1:
                # Freshly updated tasks
                task.color = 10
            elif latest_message_age_days <= 7:
                # Tasks updated in the last week
                task.color = 3
            elif latest_message_age_days <= 14:
                # Tasks updated in the last two weeks
                task.color = 2
            else:
                # Task hasn't been updated in two weeks
                task.color = 1
