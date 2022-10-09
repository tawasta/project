from odoo import models
from odoo import fields


class Partner(models.Model):
    _inherit = "res.partner"

    sla_policy_id = fields.Many2one(string="Service level", comodel_name="sla.policy")
