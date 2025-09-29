from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    task_to_sale_line_default_product_id = fields.Many2one(
        "product.product",
        string="Default Product for Task to Sale Line",
    )
