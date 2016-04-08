# -*- coding: utf-8 -*-
from openerp import models, api


class ProjectProject(models.Model):

    _inherit = 'project.project'

    @api.one
    def unlink(self):
        ''' Deactivates the project instead of deleting,
        unless the project is already deactivated '''

        if self.active:
            self.active = False
        else:
            super(ProjectProject, self).unlink()