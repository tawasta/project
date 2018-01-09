# -*- coding: utf-8 -*-
from odoo import models, api
from odoo import SUPERUSER_ID


class ProjectTask(models.Model):

    _inherit = 'project.task'

    @api.one
    def unlink(self):
        # Deactivates the project instead of deleting
        # Admin can delete archived projects

        if self.active:
            # Archive an active record
            self.active = False

        elif self.env.user_id == SUPERUSER_ID:
            # If superuser, delete the record
            super(ProjectTask, self).unlink()