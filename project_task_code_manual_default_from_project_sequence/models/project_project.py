from odoo import fields, models


class ProjectProject(models.Model):
    _inherit = "project.project"

    number_next_task = fields.Integer(
        string="Next Task Number",
        default=1,
        copy=False,
        help="Suffix number to be given to the next task's code",
    )
