# -*- coding: utf-8 -*-

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from openerp import api, fields, models

# 4. Imports from Odoo modules:
import openerp.addons.decimal_precision as dp


# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class ProjectTaskMaterials(models.Model):
    
    # 1. Private attributes
    _inherit = 'project.task.materials'

    # 2. Fields declaration
    unit_price = fields.Float("Unit price", digits=dp.get_precision('Account'))
    to_invoice = fields.Many2one('hr_timesheet_invoice.factor')

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration

    # 5. Constraints and onchanges
    @api.onchange('product_id')
    def onchange_product_id_update_price(self):
        self.unit_price = self.product_id.lst_price

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
