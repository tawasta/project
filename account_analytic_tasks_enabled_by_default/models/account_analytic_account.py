# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class AccountAnalyticAccount(models.Model):

    _inherit = 'account.analytic.account'

    @api.model
    def _trigger_project_creation(self, vals):
        '''Modify the trigger function so that project is left uncreated only
        if the Use Tasks is specifically left unchecked. This way project 
        creation gets triggered also when the user uses Quick Create to create 
        an analytic account without opening the Quick Create and Edit 
        form view'''

        if vals.get('use_tasks', True) \
            and 'project_creation_in_progress' not in self.env.context:
            return True
        else:
            return False

    use_tasks = fields.Boolean(default=True)