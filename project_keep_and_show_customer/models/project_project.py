from odoo import api, models


class ProjectProject(models.Model):
    _inherit = "project.project"

    @api.depends("allow_billable", "partner_id.company_id")
    def _compute_partner_id(self):
        pass
