from odoo import fields, models


class CrmLead(models.Model):

    _inherit = "crm.lead"

    task_id = fields.Many2one(
        comodel_name="project.task",
        string="Task",
        readonly=True,
        copy=False,
    )
