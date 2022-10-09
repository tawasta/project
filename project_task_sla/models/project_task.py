from odoo import models, fields, api


class ProjectTask(models.Model):
    _inherit = "project.task"

    sla_policy_id = fields.Many2one(string="Service level", comodel_name="sla.policy")

    @api.onchange("partner_id")
    def onchange_partner_id(self):
        for record in self:
            if record.partner_id and record.partner_id.sla_policy_id:
                record.sla_policy_id = record.partner_id.sla_policy_id

    @api.model
    def create(self, vals):
        partner_id = vals.get("partner_id")

        # When creating a new task, get SLA from partner
        if partner_id and not vals.get("sla_policy_id"):
            vals["sla_policy_id"] = (
                self.env["res.partner"].browse([partner_id]).sla_policy_id
            ).id

        return super().create(vals)
