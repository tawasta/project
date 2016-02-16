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

    accuracy = fields.Float(_("Estimation accuracy"), help="Difference between Planned Hours and Time Spent", compute='compute_accuracy')
    real_planned = fields.Float(_("Planned Hours"), help="Sum of planned hours of all tasks related to this project and its child projects.", compute='compute_real_planned')
    real_effective = fields.Float(_("Effective Hours"), help="Sum of spent hours of all tasks related to this project and its child projects.", compute='compute_real_effective')

    priority = fields.Selection([
        ('0', 'Low'),
        ('1', 'Normal'),
        ('2', 'High')
        ],
        'Priority',
        select=True,
        default="1",
    )
    project_type = fields.Many2many(
        "project.category",
        "project_category_rel",
        string="Project type"
    )

    # 3. Default methods
    @api.model
    def default_get(self, fields):
        res = super(ProjectExtension, self).default_get(fields)
        res['parent_id'] = False
        return res

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

class ProjectTask(models.Model):
    
    _inherit = 'project.task'

    # Default methods declared before fields, so using lambdas ins't needed.
    # Default value to date_start from project
    @api.model
    def _get_default_date_start(self):

        project_id = self._get_default_project_id()
        project = self.env['project.project'].search([('id', '=', project_id)])
        return project.date_start or False

    # Default value to date_end from project
    @api.model
    def _get_default_date_end(self):
        project_id = self._get_default_project_id()
        project = self.env['project.project'].search([('id', '=', project_id)])
        return project.date or False

    date_start = fields.Datetime(default=_get_default_date_start)
    date_end = fields.Datetime(default=_get_default_date_end)
    
    hour_type = fields.Selection([('fixed', 'Fixed'), 
        ('time_based', 'Time Based'), 
        ('product_development', 'Product Development'),
        ('internal', 'Internal')], 
        string='Hour type', help='Define hour type for task.')
