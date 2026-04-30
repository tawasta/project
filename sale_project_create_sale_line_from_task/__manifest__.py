##############################################################################
#
#    Author: Futural Oy
#    Copyright 2025- Futural Oy (https://futural.fi)
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
    "name": "Sale/Project: Create sale order line from task",
    "version": "17.0.1.0.0",
    "category": "Project",
    "summary": "WIP",
    "website": "https://github.com/tawasta/project",
    "author": "Futural",
    "license": "AGPL-3",
    "application": False,
    "installable": False,
    "depends": [
        "sale_project",
        "sale_order_header_text",
        "project",
        "project_task_code",
        "product",
    ],
    "data": [
        "wizards/create_sale_line_wizard_views.xml",
        "views/project_task.xml",
        "views/res_config_settings.xml",
        "security/ir_model_access.xml",
    ],
}
