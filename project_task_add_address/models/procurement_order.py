# -*- coding: utf-8 -*-


from odoo import models


class ProcurementOrder(models.Model):

    _inherit = 'procurement.order'

    def _create_service_task(self):

        res = super(ProcurementOrder, self)._create_service_task()

        add_description = ""

        if hasattr(self.env['sale.order'], 'description'):
            if self.sale_line_id.order_id.description:
                add_description = " / " + self.sale_line_id.order_id.description

        res.name = '%s: %s / %s%s' % (self.origin or '', 
                self.product_id.name,
                self.sale_line_id.order_id.partner_shipping_id.name,
                add_description)

        return res
