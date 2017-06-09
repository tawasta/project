# -*- coding: utf-8 -*-

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from openerp import api, fields, models

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class ProjectTask(models.Model):
    # 1. Private attributes
    _inherit = 'project.task'

    # 2. Fields declaration
    task_type = fields.Many2one(
        comodel_name='project.task.class',
        string='Task Type',
        help='Define task type.',
    )

    hour_type = fields.Selection(
        selection=[
            ('fixed', 'Fixed'),
            ('time_based', 'Time-Based'),
            ('product_development', 'Product Development'),
            ('internal', 'Internal'),
            ('support', 'Support')
        ],
        string='Hour type',
        help='Defines hour type for task.',
    )

    skills = fields.Many2one(
        comodel_name='hr.skill',
        string='Required skills',
    )

    # 3. Default methods

    # 4. Compute and search fields

    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
