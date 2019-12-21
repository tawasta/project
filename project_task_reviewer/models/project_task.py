# -*- coding: utf-8 -*-
from odoo import fields, models


class ProjectTask(models.Model):
    _inherit = 'project.task'

    reviewer_id = fields.Many2one(
        comodel_name='res.users',
        string='Reviewer',
        track_visibility='always'
    )

    def _message_get_auto_subscribe_fields(
            self, updated_fields, auto_follow_fields=None):
        """
        Add reviewer to followers
        """
        res = super(ProjectTask, self)._message_get_auto_subscribe_fields(
            updated_fields, auto_follow_fields
        )

        res.append('reviewer_id')

        return res
