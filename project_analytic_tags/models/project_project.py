from odoo import models, fields


class ProjectProject(models.Model):

    _inherit = 'project.project'

    analytic_tag_ids = fields.Many2many(
        comodel_name='account.analytic.tag',
        string='Analytic tags',
    )
