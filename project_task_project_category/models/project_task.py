from odoo import fields
from odoo import models


class ProjectTask(models.Model):
    _inherit = "project.task"

    project_type_id = fields.Many2one(
        string="Project type",
        comodel_name="project.type",
        related="project_id.type_id",
        store=True,
    )
