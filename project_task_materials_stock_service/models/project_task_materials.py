# -*- coding: utf-8 -*-

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from openerp import api, fields, models

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class ProjectTaskMaterials(models.Model):
    
    # 1. Private attributes
    _inherit = 'project.task.materials'

    # 2. Fields declaration

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration

    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
    @api.multi
    def create_stock_move(self):
        for line in self:
            # Don't make stock moves for services
            if line.product_id.type == 'service':
                continue

            move_id = self.env['stock.move'].create(
                line._prepare_stock_move())
            line.stock_move_id = move_id.id