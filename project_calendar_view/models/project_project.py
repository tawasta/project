# -*- coding: utf-8 -*-
from odoo import models, fields


class ProjectProject(models.Model):

    _inherit = 'project.project'

    color = fields.Char(
        string='Color',
    )
