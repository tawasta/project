from odoo import models


class ProjectTask(models.Model):

    _inherit = "project.task"

    def write(self, vals):
        if "stage_id" in vals and "user_id" not in vals:
            for record in self:
                if not record.user_id:
                    record.user_id = self.env.user.id

        return super().write(vals)
