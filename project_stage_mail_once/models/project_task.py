from odoo import fields, models


class ProjectTask(models.Model):
    _inherit = "project.task"

    mail_template_once_sent = fields.Boolean(
        string="Stage Email Template Sent Once",
        copy=False,
    )

    def _track_template(self, changes):
        res = super()._track_template(changes)

        task = self[0]
        stage = task.stage_id

        if "stage_id" in res and stage.mail_template_send_once:
            if task.mail_template_once_sent:
                res.pop("stage_id")
            else:
                task.sudo().mail_template_once_sent = True

        return res
