from odoo import models


class ProjectTask(models.Model):
    _inherit = "project.task"

    def write(self, vals):
        if "stage_id" in vals and "user_ids" not in vals:
            for record in self:
                if not record.user_ids:
                    # Päivitetään käyttäjä Many2many-kenttään oikein
                    vals["user_ids"] = [(4, self.env.user.id)]

        return super().write(vals)
