# -*- coding: utf-8 -*-
from odoo import models, api
from odoo import SUPERUSER_ID


class ProjectTask(models.Model):

    _inherit = 'project.task'

    @api.multi
    def unlink(self):
        # Deactivates the project instead of deleting
        # Admin can delete archived projects

        for record in self:
            if record.active:
                # Archive an active record
                record.active = False

            elif record.env.user_id == SUPERUSER_ID:
                # If superuser, delete the record
                super(ProjectTask, record).unlink()
