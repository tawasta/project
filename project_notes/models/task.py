from odoo import fields, models


class ProjectTask(models.Model):
    _inherit = "project.task"

    note_ids = fields.One2many("project.task.note", "task_id", "Task notes")
