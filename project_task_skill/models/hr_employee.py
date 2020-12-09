from odoo import api
from odoo import fields
from odoo import models


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    skills_ids = fields.Many2many(
        comodel_name="hr.skill", compute="_compute_skill_ids", string="Employee skills",
    )

    @api.onchange("skill_ids")
    @api.depends("skill_ids")
    def _compute_skill_ids(self):
        for record in self:
            record.skill_ids = record.skill_ids.mapped("skill_id")
