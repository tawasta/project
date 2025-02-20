from odoo import api, models


class ProjectTask(models.Model):
    _inherit = "project.task"

    @api.depends("parent_id.partner_id", "project_id")
    def _compute_partner_id(self):
        for task in self:
            if task.partner_id:
                if task.project_id.partner_id:
                    task.partner_id = task.project_id.partner_id
            else:
                task.partner_id = (
                    task.project_id.partner_id or task.parent_id.partner_id
                )
