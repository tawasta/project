from odoo import api, fields, models

class ProjectTask(models.Model):
    _inherit = "project.task"

    project_task_sla_id = fields.Many2one("project.task.sla", string="SLA")
    sla_met = fields.Boolean(
        string="SLA Met", compute="_compute_sla_status", store=True
    )
    sla_diff_hours = fields.Float(
        string="SLA Diff (hours)", compute="_compute_sla_status", store=True
    )

    @api.depends("project_task_sla_id.response_time", "create_date", "date_deadline")
    def _compute_sla_status(self):
        for task in self:
            if task.create_date and task.date_deadline and task.project_task_sla_id:
                diff = (task.date_deadline - task.create_date).total_seconds() / 3600
                task.sla_diff_hours = diff - task.project_task_sla_id.response_time
                task.sla_met = task.sla_diff_hours <= 0
            else:
                task.sla_diff_hours = 0.0
                task.sla_met = False
