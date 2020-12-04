##############################################################################
#
#    Author: Oy Tawasta OS Technologies Ltd.
#    Copyright 2020 Oy Tawasta OS Technologies Ltd. (https://tawasta.fi)
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
    "name": "Update task end date when moving task to closed stage",
    "summary": "Task end date is updated when task is moved to a ended stage",
    "version": "12.0.1.0.0",
    "category": "Project Management",
    "website": "https://github.com/Tawasta/project",
    "author": "Tawasta",
    "license": "AGPL-3",
    "depends": ["project", "project_stage_closed"],
    "data": [],
    "installable": True,
    "auto-install": False,
}
