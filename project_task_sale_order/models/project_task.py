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
    sale_order = fields.Many2one(
        'sale.order',
        string='Sale order',
        compute='compute_sale_order',
        store=True,
        readonly=True
    )
    sale_order_lines = fields.One2many(
        'sale.order.line',
        'order_id',
        string='Order Lines',
        compute='compute_sale_order_lines',
        inverse='compute_sale_order_lines_inverse',
    )
    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration
    @api.multi
    @api.depends('sale_line_id')
    def compute_sale_order(self):
        for record in self:
            record.sale_order = record.sale_line_id.order_id.id

    @api.multi
    def compute_sale_order_lines(self):
        for record in self:
            if record.sale_order:
                record.sale_order_lines = record.sale_order.order_line

    @api.multi
    def compute_sale_order_lines_inverse(self):
        for record in self:
            if record.sale_order:
                record.sale_order.order_line = record.sale_order_lines

    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
