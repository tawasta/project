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
    contract = fields.Many2one(
        'account.analytic.account',
        string='Contract',
        compute='compute_contract',
        store=False,
        readonly=True
    )

    contract_partner = fields.Many2one(
        'res.partner',
        string='Contract partner',
        compute='compute_contract_partner',
        store=False,
        readonly=True
    )

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration
    @api.multi
    def compute_contract(self):
        for record in self:
            record.contract = record.sale_order.project_id.id

    @api.multi
    def compute_contract_partner(self):
        for record in self:
            record.contract_partner = record.contract.partner_id.id

    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
