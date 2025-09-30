import logging

from odoo import _, fields, models

_logger = logging.getLogger(__name__)


class SaleCreateLineFromTaskWizard(models.TransientModel):
    _name = "sale.create.line.from.task.wizard"
    _description = "Wizard to create sale order line from task"

    task_id = fields.Many2one("project.task", string="Task", required=True)
    partner_id = fields.Many2one("res.partner", string="Partner", required=True)
    sale_order_id = fields.Many2one(
        "sale.order",
        string="Sale Order",
        help="Parent order for the new sale order line. If you do not select one, a "
        "new sale order will be created",
    )

    sale_order_header_text = fields.Char(
        related="sale_order_id.header_text", readonly=1
    )

    product_id = fields.Many2one("product.product", string="Product", required=True)

    def _prepare_sale_order_values(self):
        return {"partner_id": self.partner_id.id}

    def _prepare_sale_line_values(self):
        active_task = self.env["project.task"].search([("id", "=", self.task_id.id)])

        res = {
            "order_id": self.sale_order_id.id,
            "product_id": self.product_id.id,
            "product_uom_qty": active_task.allocated_hours or 0.0,
        }

        return res

    def default_get(self, fields_list):
        # Prepopulate the wizard

        res = super().default_get(fields_list)

        active_task_id = self.env.context.get("default_task_id")
        res["task_id"] = active_task_id
        res["partner_id"] = self.env.context.get("default_partner_id")

        active_task = self.env["project.task"].search(
            [("id", "=", active_task_id)], limit=1
        )

        res["product_id"] = (
            active_task.company_id.task_to_sale_line_default_product_id
            and active_task.company_id.task_to_sale_line_default_product_id.id
            or False
        )

        return res

    def action_create_sale_line(self):
        # Create SO line, link it to the task, and post chatter messages to
        # task and Sale Order records

        self.ensure_one()

        # If sale order was not selected, create one first
        if not self.sale_order_id:
            sale_order_obj = self.env["sale.order"]
            sale_order_vals = self._prepare_sale_order_values()
            new_sale_order = sale_order_obj.create(sale_order_vals)
            self.sale_order_id = new_sale_order.id

        sale_order_line_obj = self.env["sale.order.line"]
        sale_line_vals = self._prepare_sale_line_values()

        new_sale_line = sale_order_line_obj.create(sale_line_vals)

        # Append task code and name to end of SO line's name
        new_sale_line.name = (
            f"{new_sale_line.name}: {self.task_id.code} {self.task_id.name}"
        )

        sale_line_msg = _(
            "New Sale Order Line created from project task %(code)s - %(name)s"
        ) % {"code": self.task_id.code, "name": self.task_id.name}

        new_sale_line.order_id.message_post(body=sale_line_msg)

        active_task = self.env["project.task"].search([("id", "=", self.task_id.id)])

        active_task.sale_line_id = new_sale_line.id

        task_msg = _(
            "New Sale Order Line created for %(name)s with %(hours)s allocated hours"
        ) % {
            "name": new_sale_line.order_id.name,
            "hours": active_task.allocated_hours,
        }

        active_task.message_post(body=_(task_msg))
