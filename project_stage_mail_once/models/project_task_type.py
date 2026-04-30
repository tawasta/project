from odoo import fields, models


class ProjectTaskType(models.Model):
    _inherit = "project.task.type"

    mail_template_send_once = fields.Boolean(
        string="Send Email Template Only Once",
        help="If enabled, this stage email template is sent only the first time a task reaches this stage.",
    )