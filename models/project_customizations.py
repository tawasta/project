# -*- coding: utf-8 -*-

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from openerp import api, fields, models

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class ProjectCustomizations(models.Model):
    
    # 1. Private attributes
    _inherit = 'project.project'

    # 2. Fields declaration
    project_type = fields.Many2one(
        "project.type",
        string="Project type"
    )

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration

    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods

class ProjectTask(models.Model):
    
    _inherit = 'project.task'

    hour_type = fields.Selection([('fixed', 'Fixed'), 
        ('time_based', 'Time-Based'), 
        ('product_development', 'Product Development'),
        ('internal', 'Internal')], 
        string='Hour type', help='Define hour type for task.')

class ProjectType(models.Model):

    _name = 'project.type'

    name = fields.Char(string='Name', required='True', translate=True)
