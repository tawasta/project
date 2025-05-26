import logging

from odoo import api, models

_logger = logging.getLogger(__name__)


class Project(models.Model):
    _inherit = "project.project"

    @api.model_create_multi
    def create(self, vals_list):
        # Rename the created project

        if self.env.context.get("project_name_from_sale_order_line", False):
            sale_order_line_obj = self.env["sale.order.line"]

            for vals in vals_list:
                if vals.get("sale_line_id", False):
                    sale_order_line = sale_order_line_obj.search(
                        [("id", "=", vals.get("sale_line_id"))]
                    )

                    vals["name"] = sale_order_line.name

        return super().create(vals_list)
