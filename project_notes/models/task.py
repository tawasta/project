# -*- coding: utf-8 -*-

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from odoo import fields, models


# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class ProjectTask(models.Model):
    # 1. Private attributes
    _inherit = 'project.task'

    # 2. Fields declaration
    note_ids = fields.One2many(
        "project.task.note",
        'task_id',
        'Task notes'
    )

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration

    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods


class TaskNote(models.Model):
    # 1. Private attributes
    _name = 'project.task.note'

    # 2. Fields declaration
    name = fields.Char("Title", size=256)
    note = fields.Text("Note")
    done = fields.Boolean(
        "Done",
        help="Informative tag for the note. Has no functionality")
    task_id = fields.Many2one("project.task", "Task")

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration

    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
