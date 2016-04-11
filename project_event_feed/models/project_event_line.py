# -*- coding: utf-8 -*-

# 1. Standard library imports:

# 2. Known third party imports:
import re
# 3. Odoo imports (openerp):
from openerp import api, fields, models, tools, _

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


# Transient model to represent project's feed
class ProjectEventLine(models.TransientModel):
    # 1. Private attributes
    _name = 'project.event.line'

    # 2. Fields declaration
    task_id = fields.Many2one('project.task', string='Task')
    name = fields.Char(string='Event description')
    unit_amount = fields.Float(string='Time used')
    time_left = fields.Float(string='Time remaining')
    user_id = fields.Many2one('res.users', string='Done by')
    project_id = fields.Many2one('project.project', string='Project')
    date = fields.Datetime(string='Date')

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration

    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
