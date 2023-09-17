from odoo import api, fields, models


class ProjectTask(models.Model):

    _inherit = "project.task"

    def _compute_task_color(self):
        for record in self:
            if not record.message_ids:
                # There shouldn't really be any cases where task has no messages,
                # but check it just in case
                continue
            latest_message = record.message_ids[0]
            latest_message_age = fields.Datetime.now() - latest_message.date
            latest_message_age_days = latest_message_age.days
            project = record.project_id

            if latest_message_age_days <= project.task_autocolor_days_fresh:
                # Freshly updated tasks
                record.color = project.task_autocolor_color_fresh
            elif latest_message_age_days <= project.task_autocolor_days_recent:
                # Tasks updated recently
                record.color = project.task_autocolor_color_recent
            elif latest_message_age_days <= project.task_autocolor_days_aged:
                # Aged tasks
                record.color = project.task_autocolor_color_aged
            else:
                # Stale tasks
                record.color = 1

    @api.returns("mail.message", lambda value: value.id)
    def message_post(self, *args, **kwargs):
        res = super().message_post(
            *args,
            **kwargs,
        )

        # Recompute color
        self._compute_task_color()

        return res
