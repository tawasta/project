##############################################################################
#
#    Author: Oy Tawasta OS Technologies Ltd.
#    Copyright 2022- Oy Tawasta OS Technologies Ltd. (https://tawasta.fi)
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
from odoo import api, fields, models

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class ProjectTask(models.Model):
    # 1. Private attributes
    _inherit = "project.task"

    # 2. Fields declaration
    # Complete override of priority field to add custom values
    priority = fields.Selection(
        [
            ("0", "Unspecified"),
            ("1", "Urgent"),
            ("2", "Very Urgent"),
            ("3", "Immediate"),
        ],
        default="0",
        index=True,
        readonly=True,
        store=True,
        compute="_compute_priority",
        help="Task priority is calculated from task scope and service-level agreement.",
    )
    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration
    @api.depends("sla_id", "scope_id")
    def _compute_priority(self):
        for task in self:
            if task.sla_id and task.scope_id:
                # sla critial or average, scope easy or medium
                if task.sla_id.value < 3 and task.scope_id.value >= 3:
                    task.priority = "3"
                # sla low or development, scope difficult or to be defined
                elif task.sla_id.value >= 3 and task.scope_id.value < 3:
                    task.priority = "1"
                else:
                    task.priority = "2"
            else:
                task.priority = "0"

    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
