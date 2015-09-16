# -*- coding: utf-8 -*-
from openerp import models, api


class ProjectTask(models.Model):

    _inherit = 'project.task'

    @api.one
    def unlink(self):
        ''' Cancels the task instead of deleting,
        unless the task is already canceled '''

        stage = self.stage_id
        stage_cancel = self.env['project.task.type'].search([('name', 'ilike', 'cancel')])
        
        if stage == stage_cancel:
            super(ProjectTask, self).unlink()
        else:
            self.stage_id = stage_cancel