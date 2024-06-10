from odoo import fields, models


class ProjectTask(models.Model):

    _inherit = "project.task"

    priority = fields.Selection(
        [
            ("0", "P3"),
            ("1", "P2"),
            ("2", "P1"),
            ("3", "P0"),
        ]
    )
