
from odoo import fields, models


class ProjectTask(models.Model):

    _inherit = 'project.task'

    company_id = fields.Many2one(required=False)
