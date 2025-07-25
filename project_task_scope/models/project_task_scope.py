from odoo import fields, models


class ProjectTaskScope(models.Model):
    _name = "project.task.scope"
    _description = "Task Scope"

    name = fields.Char(required=True, translate=True)
    level = fields.Selection(
        [
            ("1", "Easy"),
            ("2", "Medium"),
            ("3", "Hard"),
            ("4", "Undefined"),
        ],
        required=True,
    )
    description = fields.Text(translate=True)
    task_ids = fields.One2many("project.task", "project_task_scope_id", string="Tasks")


class ProjectTask(models.Model):
    _inherit = "project.task"

    project_task_scope_id = fields.Many2one("project.task.scope", string="Scope")
