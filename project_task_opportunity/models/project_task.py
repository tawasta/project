from odoo import fields, models


class ProjectTask(models.Model):
    _inherit = "project.task"

    lead_ids = fields.One2many(
        comodel_name="crm.lead",
        inverse_name="task_id",
        string="Opportunities",
        readonly=True,
        copy=False,
    )
