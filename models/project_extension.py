# -*- coding: utf-8 -*-

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from openerp import api, fields, models, _

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:

class ProjectExtension(models.Model):
    
    # 1. Private attributes
    _inherit = 'project.project'
    _order = "priority DESC, sequence DESC, create_date DESC"
    
    # 2. Fields declaration

    accuracy = fields.Float(_("Estimation accuracy"),help="Difference between Planned Hours and Time Spent", compute='compute_accuracy')
    real_planned = fields.Float(_("Planned Hours"), compute='compute_real_planned')
    real_effective = fields.Float(_("Effective Hours"), compute='compute_real_effective')

    priority = fields.Selection([
        ('0', 'Low'),
        ('1', 'Normal'),
        ('2', 'High')
        ],
        'Priority',
        select=True,
        default="1",
    )

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration
    
    @api.one
    def compute_accuracy(self):

        self.accuracy = self.real_planned - self.real_effective

    @api.depends('tasks.planned_hours')
    @api.one
    def compute_real_planned(self):

        planned = 0.0
        tasks = self.env['project.task'].search([('id',
            'in', self.tasks.ids)], order='write_date DESC')
        for task in tasks:
            planned += task.planned_hours
        self.real_planned = planned

    @api.depends('tasks.effective_hours')
    @api.one
    def compute_real_effective(self):

        effective = 0.0
        tasks = self.env['project.task'].search([('id',
            'in', self.tasks.ids)], order='write_date DESC')
        for task in tasks:
            effective += task.effective_hours
        self.real_effective = effective


    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
