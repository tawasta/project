from odoo import models
from odoo import fields


class SlaPolicy(models.Model):
    _name = "sla.policy"
    _description = "Service Level Agreement Policy"

    name = fields.Char(required=True, index=True)
    description = fields.Html("Description")
    active = fields.Boolean("Active", default=True)
    sequence = fields.Integer(default=1)

    partner_ids = fields.One2many(
        string="Partners",
        comodel_name="res.partner",
        inverse_name="sla_policy_id",
    )

    project_task_ids = fields.One2many(
        string="Tasks",
        comodel_name="project.task",
        inverse_name="sla_policy_id",
    )
