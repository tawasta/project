# -*- coding: utf-8 -*-
from odoo import models, api
from odoo import SUPERUSER_ID


class ProjectProject(models.Model):

    _inherit = 'project.project'

    @api.multi
    def unlink(self):
        # Deactivates the project instead of deleting
        # Admin can delete archived projects

        if self.active:
            # Archive an active record
            self.active = False

        elif self.env.user_id == SUPERUSER_ID:
            # If superuser, delete the record
            super(ProjectProject, self).unlink()