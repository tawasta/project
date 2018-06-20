# -*- coding: utf-8 -*-
from odoo import models, api


class ProjectTask(models.Model):

    _inherit = 'project.task'

    @api.model
    def create(self, vals):
        if self._context.get('default_project_id'):
            self.check_locked(self._context.get('default_project_id'))

        return super(ProjectTask, self).create(vals)

    @api.multi
    def write(self, vals):
        self.check_locked()

        return super(ProjectTask, self).write(vals)

    @api.multi
    def unlink(self):
        self.check_locked()

        return super(ProjectTask, self).unlink()

    def check_locked(self, project_id=False):
        if project_id:
            project = self.env['project.project'].browse([project_id])
        else:
            project = self.project_id

        project.check_locked()

        return
