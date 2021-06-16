from odoo import fields, models


class ProjectNote(models.Model):
    _name = "project.project.note"

    name = fields.Char("Title", size=256)
    note = fields.Text("Note")
    project_id = fields.Many2one("project.project", "Project")
