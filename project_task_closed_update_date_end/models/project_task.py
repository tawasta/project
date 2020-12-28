from odoo import api
from odoo import fields
from odoo import models


class ProjectTask(models.Model):
    _inherit = "project.task"

    @api.model
    def create(self, vals):
        if vals.get("stage_id"):
            vals.update(self.update_date_end(vals["stage_id"]))

        return super(ProjectTask, self).create(vals)

    @api.multi
    def write(self, vals):
        if vals.get("stage_id"):
            vals.update(self.update_date_end(vals["stage_id"]))

        return super(ProjectTask, self).write(vals)

    def update_date_end(self, stage_id):
        project_task_type = self.env["project.task.type"].browse(stage_id)
        if project_task_type.fold or project_task_type.closed:
            return {"date_end": fields.Datetime.now()}
        return {"date_end": False}
