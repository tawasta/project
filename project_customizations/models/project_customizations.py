# -*- coding: utf-8 -*-

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from openerp import api, fields, models


# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class ProjectProject(models.Model):
    # 1. Private attributes
    _inherit = 'project.project'

    # 2. Fields declaration
    project_type = fields.Many2one(
        "project.type",
        string="Project type",
        help="Defines project's type."
    )

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration

    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods


class ProjectTask(models.Model):
    _inherit = 'project.task'

    task_type = fields.Many2one(
        "task.type",
        string="Task Type",
        help="Define task's type."
    )

    hour_type = fields.Selection([
        ('fixed', 'Fixed'),
        ('time_based', 'Time-Based'),
        ('product_development', 'Product Development'),
        ('internal', 'Internal'),
        ('support', 'Support')],
        string="Hour type",
        help="Defines hour type for task."
    )

    skills = fields.Many2one(
        "hr.skill",
        string="Required skills"
    )


class ProjectType(models.Model):
    _name = 'project.type'
    _order = 'name'

    name = fields.Char(string='Name', required=True, translate=True)
    parent_id = fields.Many2one('project.type', string='Parent', ondelete='cascade')
    child_ids = fields.One2many('project.type', 'parent_id', string='Children')

    @api.multi
    def name_get(self):
        res = []
        for record in self:
            names = []
            current = record
            while current:
                names.append(current.name)
                current = current.parent_id
            res.append((record.id, ' / '.join(reversed(names))))
        return res


class TaskType(models.Model):
    _name = 'task.type'
    _order = 'name'

    name = fields.Char(string='Name', required=True, translate=True)
    parent_id = fields.Many2one('task.type', string='Parent', ondelete='cascade')
    child_ids = fields.One2many('task.type', 'parent_id', string='Children')

    @api.multi
    def name_get(self):
        res = []
        for record in self:
            names = []
            current = record
            while current:
                names.append(current.name)
                current = current.parent_id
            res.append((record.id, ' / '.join(reversed(names))))
        return res
