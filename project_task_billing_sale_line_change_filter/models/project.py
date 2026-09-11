##############################################################################
#
#    Author: Futural Oy
#    Copyright 2026 Futural Oy (https://futural.fi)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program. If not, see http://www.gnu.org/licenses/agpl.html
#
##############################################################################

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from odoo import _, api, fields, models
from odoo.exceptions import UserError

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class Task(models.Model):
    # 1. Private attributes
    _inherit = "project.task"

    _TRACKED_BILLING_FIELDS = ("billing_enabled", "sale_line_id")

    # 2. Fields declaration
    billing_sale_line_change_date = fields.Datetime(
        string="Billing / Sale Order Item Changed",
        compute="_compute_billing_sale_line_change_date",
        search="_search_billing_sale_line_change_date",
        help="Search-only field: filters tasks where 'Billing' or 'Sale "
        "Order Item' changed within a date range, based on chatter "
        "tracking (mail.tracking.value).",
    )

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration
    def _compute_billing_sale_line_change_date(self):
        for task in self:
            task.billing_sale_line_change_date = False

    def _search_billing_sale_line_change_date(self, operator, value):
        if operator not in ("=", "!=", ">", ">=", "<", "<="):
            raise UserError(
                _("Operator %s is not supported for this filter.") % operator
            )
        if not value:
            raise UserError(_("This filter requires a specific date/time value."))

        messages = (
            self.env["mail.message"]
            .sudo()
            .search(
                [
                    ("model", "=", "project.task"),
                    (
                        "tracking_value_ids.field_id.name",
                        "in",
                        list(self._TRACKED_BILLING_FIELDS),
                    ),
                    ("date", operator, value),
                ]
            )
        )
        return [("id", "in", messages.mapped("res_id"))]

    # 5. Constraints and onchanges

    # 6. CRUD methods
    @api.model_create_multi
    def create(self, vals_list):
        tasks = super().create(vals_list)
        # mail.thread only creates mail.tracking.value records for fields
        # changed by write(); a field already set at creation time never
        # gets tracked, so it would never match this module's date filter.
        # Track those tasks here the same way write() would, using "unset"
        # as the initial value.
        newly_billable = tasks.filtered(
            lambda task: any(task[fname] for fname in self._TRACKED_BILLING_FIELDS)
        )
        if newly_billable:
            initial_values = {
                task.id: dict.fromkeys(self._TRACKED_BILLING_FIELDS, False)
                for task in newly_billable
            }
            newly_billable.sudo()._message_track(
                self._TRACKED_BILLING_FIELDS, initial_values
            )
        return tasks

    # 7. Action methods

    # 8. Business methods
