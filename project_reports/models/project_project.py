# -*- coding: utf-8 -*-

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from openerp import models, fields, api

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class ProjectProject(models.Model):

	# 1. Private attributes
	_inherit = 'project.project'

	 # 2. Fields declaration
	avg_price = fields.Float("Average price", default=10.5)
	current_cost = fields.Float(compute='compute_current_cost')
	estimated_cost = fields.Float(compute='compute_estimated_cost')

	# 3. Default methods

	# 4. Compute and search fields, in the same order that fields declaration
	@api.one
	def compute_estimated_cost(self):

		arvo = self.planned_hours * self.avg_price
		self.estimated_cost = arvo;


	@api.one
	def compute_current_cost(self):
		

		arvo = self.effective_hours * self.avg_price

		self.current_cost = arvo


	# 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
    
