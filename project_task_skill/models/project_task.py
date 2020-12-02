from odoo import api
from odoo import fields
from odoo import models


class ProjectTask(models.Model):
    _inherit = "project.task"

    employee_id = fields.Many2one(comodel_name="hr.employee")
    skill_id = fields.Many2one(string="Skill", comodel_name="hr.skill")

    employee_skill_ids = fields.Many2many(
        comodel_name="hr.skill",
        string="Employee skills",
        related="employee_id.skill_ids",
    )

    @api.onchange("employee_id")
    @api.depends("employee_id")
    def onchange_employee_id_update_user(self):
        for record in self:
            if record.employee_id.user_id:
                record.user_id = record.employee_id.user_id

    @api.onchange("skill_id")
    def onchange_skill_update_user_domain(self):
        domain = []
        if self.skill_id:
            domain.append(("employee_skill_ids.skill_id", "=", self.skill_id.id))

        return {"domain": {"employee_id": domain}}
