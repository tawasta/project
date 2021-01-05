from odoo import api
from odoo import fields
from odoo import models


class ProjectTask(models.Model):
    _inherit = "project.task"

    skill_id = fields.Many2one(string="Required skill", comodel_name="hr.skill")

    employee_skill_ids = fields.Many2many(
        comodel_name="hr.skill",
        string="Employee skills",
        compute="_compute_employee_skill_ids",
    )

    @api.onchange("skill_id")
    def onchange_skill_update_user_domain(self):
        domain = []
        if self.skill_id:
            domain.append(("skill_ids", "=", self.skill_id.id))

        return

        return {"domain": {"employee_id": domain}}

    def _compute_employee_skill_ids(self):
        for record in self:
            if not record.employee_id:
                continue
            record.employee_skill_ids = record.employee_id.skill_ids
