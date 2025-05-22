from odoo import fields, models


class Task(models.Model):
    _inherit = "project.task"

    code = fields.Char(
        string="Task Number",
        required=False,
        default="/",
        copy=False,
    )
