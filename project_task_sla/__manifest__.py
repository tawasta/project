##############################################################################
#
#    Author: Oy Tawasta OS Technologies Ltd.
#    Copyright 2019- Oy Tawasta OS Technologies Ltd. (https://tawasta.fi)
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

{
    "name": "Project Task SLA",
    "summary": "Add SLA to tasks",
    "version": "14.0.1.0.0",
    "category": "Project",
    "website": "https://gitlab.com/tawasta/odoo/helpdesk",
    "author": "Tawasta",
    "license": "AGPL-3",
    "depends": [
        "project",
    ],
    "data": [
        "security/ir_model_access.xml",
        "views/partner.xml",
        "views/project_task.xml",
        "views/sla_policy_form.xml",
        "views/sla_policy_menu.xml",
        "views/sla_policy_tree.xml",
    ],
    "application": False,
    "installable": True,
}
