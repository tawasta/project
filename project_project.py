# -*- coding: utf-8 -*-

from openerp import models, fields

class ProjectProject(models.Model):

	_inherit = 'project.project'

	avg_price = fields.Float("Average price", default=10.5)

