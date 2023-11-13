from odoo import fields, models


class ProjectTask(models.Model):

    _inherit = "project.task"

    def write(self, vals):
        # This does the exact same thing as core "project"-module,
        # as the one in project-module doesn't work
        if "stage_id" in vals:
            project_task_type = self.env["project.task.type"].browse(vals["stage_id"])
            if project_task_type.fold or project_task_type.is_closed:
                vals["date_end"] = fields.Datetime.now()

        return super().write(vals)
