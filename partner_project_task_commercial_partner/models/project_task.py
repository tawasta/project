from odoo import fields
from odoo import models


class ProjectTask(models.Model):

    _inherit = "project.task"

    commercial_partner_id = fields.Many2one(
        comodel_name="res.partner",
        string="Commercial Entity",
        related="partner_id.commercial_partner_id",
        store=True,
        index=True,
    )
