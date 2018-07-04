# -*- coding: utf-8 -*-
from odoo import models, api, fields


class ProjectProject(models.Model):

    _inherit = 'project.project'

    @api.multi
    def write(self, values):
        if 'active' in values and not values['active']:
            if not self.date and 'date' not in values:
                values['date'] = fields.Date.today()

        return super(ProjectProject, self).write(values)

    @api.model
    def create(self, values):
        # Set this on create instead of field default, so it will not
        # preset existing empty start dates on install

        if not values.get('date_start'):
            values['date_start'] = fields.Date.today()

        return super(ProjectProject, self).create(values)
