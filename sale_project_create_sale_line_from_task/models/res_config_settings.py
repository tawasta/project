from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    task_to_sale_line_default_product_id = fields.Many2one(
        "product.product",
        string="Default Product for Task to Sale Line",
        related="company_id.task_to_sale_line_default_product_id",
        readonly=False,
    )
