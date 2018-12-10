# -*- coding: utf-8 -*-

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from odoo import api, fields, models

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class ProjectType(models.Model):
    # 1. Private attributes
    _name = 'project.type'
    _order = 'name'

    # 2. Fields declaration
    name = fields.Char(
        string='Name',
        required=True,
        translate=True
    )
    parent_id = fields.Many2one(
        comodel_name='project.type',
        string='Parent',
        ondelete='cascade'
    )
    child_ids = fields.One2many(
        comodel_name='project.type',
        inverse_name='parent_id',
        string='Children'
    )

    # 3. Default methods
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

    # 4. Compute and search fields

    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
