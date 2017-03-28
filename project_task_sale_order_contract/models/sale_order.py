# -*- coding: utf-8 -*-

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from openerp import api, fields, models
from openerp import _

# 4. Imports from Odoo modules:
from openerp.exceptions import ValidationError

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class SaleOrder(models.Model):
    
    # 1. Private attributes
    _inherit = 'sale.order'

    # 2. Fields declaration
    contract_partner = fields.Many2one(
        'res.partner',
        string='Contract partner',
        compute='compute_contract_partner',
        store=True,
        readonly=True
    )
    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration

    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods
    @api.multi
    @api.depends('project_id')
    def compute_contract_partner(self):
        for record in self:
            record.contract_partner = record.project_id.partner_id.id

    # 8. Business methods
