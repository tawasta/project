# -*- coding: utf-8 -*-
from odoo import fields, models


class ProjectIssue(models.Model):
    _inherit = 'project.issue'

    class_id = fields.Many2one(
        comodel_name='project.task.class',
        string='Class',
    )
