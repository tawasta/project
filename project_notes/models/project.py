from odoo import fields, models


class ProjectProject(models.Model):
    _inherit = "project.project"

    note_ids = fields.One2many("project.project.note", "project_id", "Project notes")
