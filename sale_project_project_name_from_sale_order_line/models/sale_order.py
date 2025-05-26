import logging

from odoo import models

_logger = logging.getLogger(__name__)


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def _action_confirm(self):
        # Pass in context info that renaming should be done
        return super(
            SaleOrder, self.with_context(project_name_from_sale_order_line=True)
        )._action_confirm()
