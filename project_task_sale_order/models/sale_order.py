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
    tasks = fields.One2many('project.task', 'sale_order', string='Tasks')
    open_tasks = fields.One2many('project.task', 'sale_order', string='Tasks', domain=[('stage_id.closed', '=', False)])

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration

    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods
    @api.multi
    def action_invoice_create(self, grouped=False, states=None, date_invoice=False):

        for record in self:
            if record.open_tasks:
                error = _("This sale has open tasks. Please close them before invoicing.")
                raise ValidationError(error)

        res = super(SaleOrder, self).action_invoice_create(
            grouped=grouped,
            states=states,
            date_invoice=date_invoice
        )

        return res

    # 8. Business methods
