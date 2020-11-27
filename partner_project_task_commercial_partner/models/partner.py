from odoo import models, api


class Partner(models.Model):

    _inherit = "res.partner"

    def _compute_task_count(self):
        for record in self:
            record.task_count = self.env["project.task"].search_count(
                [("commercial_partner_id", "=", record.commercial_partner_id.id),]
            )
