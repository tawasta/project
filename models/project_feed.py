# -*- coding: utf-8 -*-

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from openerp import api, fields, models

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class ProjectFeed(models.Model):

	# 1. Private attributes
	_inherit = 'project.project'

	# 2. Fields declaration
	task_work = fields.One2many(
		'project.task.work',
		'task_id',
		string='Work lines',
		compute='compute_task_lines'
	)

	# 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration
	@api.one
	def compute_task_lines(self):

		# Get the project_task_works and order them DESC by write_date
		self.task_work = self.env['project.task.work'].search([('task_id',
			'in', self.tasks.ids)], order='write_date DESC')

	# 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
    
