##############################################################################
#
#    Author: Futural Oy
#    Copyright 2023 Futural Oy (https://futural.fi)
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
    "name": "Installation Checklist (Module-driven)",
    "summary": "Installation Checklist (Module-driven)",
    "version": "17.0.1.0.0",
    "category": "Project",
    "website": "https://github.com/tawasta/project",
    "author": "Futural",
    "license": "AGPL-3",
    "depends": [
        "project",
        "mail",
        "software_knowledge_base",
    ],
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "views/checklist_views.xml",
        "views/installation_views.xml",
        "views/module_views.xml",
        "views/project_views.xml",
    ],
    "demo": [],
    "application": False,
    "installable": True,
}
