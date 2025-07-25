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
    "name": "Project: Manual Code for Tasks: Get Default from Project Sequence",
    "version": "17.0.1.0.1",
    "category": "Project",
    "summary": "Autofills the manual code field from project sequence "
    "and task running number",
    # Alpha to match project_sequence and not trigger precommit failure
    "development_status": "Alpha",
    "website": "https://github.com/tawasta/project",
    "author": "Futural",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": ["project_task_code", "project_sequence"],
    "data": [
        "views/project_project.xml",
    ],
}
