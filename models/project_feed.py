# -*- coding: utf-8 -*-

from openerp import api, fields, models

class ProjectFeed(models.Model):

	_inherit = 'project.project'

	task_work = fields.One2many(
		'project.task.work',
		'task_id',
		string='Work lines',
		compute='compute_task_lines'
	)

	@api.one
	def compute_task_lines(self):

		# Get the project_task_works and order them DESC by write_date
		self.task_work = self.env['project.task.work'].search([('task_id',
			'in', self.tasks.ids)], order='write_date DESC')


