from odoo import fields, models


class ProjectTaskSLA(models.Model):
    _name = "project.task.sla"
    _description = "Task SLA"

    name = fields.Char(required=True, translate=True)
    criticality = fields.Selection(
        [
            ("1", "SLA 1 - Critical"),
            ("2", "SLA 2 - Medium"),
            ("3", "SLA 3 - Low"),
            ("4", "SLA 4 - Development"),
        ],
        required=True,
    )
    response_time = fields.Float(string="Response Time (hours)")
    description = fields.Text(translate=True)
    task_ids = fields.One2many("project.task", "project_task_sla_id", string="Tasks")
