# -*- coding: utf-8 -*-

from openerp import models, fields, api

class ProjectProject(models.Model):

	_inherit = 'project.project'

	avg_price = fields.Float("Average price", default=10.5)


	current_cost = fields.Float(compute='compute_current_cost')
	estimated_cost = fields.Float(compute='compute_estimated_cost')

	@api.one
	def compute_estimated_cost(self):

		arvo = self.planned_hours * self.avg_price
		self.estimated_cost = arvo;


	@api.one
	def compute_current_cost(self):
		

		arvo = self.effective_hours * self.avg_price

		self.current_cost = arvo



