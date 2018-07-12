# -*- coding: utf-8 -*-
from odoo import models, api


class ProjectProject(models.Model):

    _inherit = 'project.project'

    @api.multi
    def toggle_active(self):
        super(ProjectProject, self).toggle_active()

        for record in self:
            # If analytic account has no open projects anymore, close it
            projects = self.search([
                ('analytic_account_id', '=', record.analytic_account_id.id),
            ])

            if not projects:
                record.analytic_account_id.active = False
