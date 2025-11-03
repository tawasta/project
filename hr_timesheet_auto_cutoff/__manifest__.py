##############################################################################
#
#    Author: Futural Oy
#    Copyright 2022- Futural Oy (https://futural.fi)
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
    "name": "Timesheet Auto Stop at Cutoff",
    "summary": """
    Auto-stop running timesheet timers at a daily cutoff (global + per-employee)""",
    "version": "17.0.1.0.0",
    "category": "Project",
    "website": "https://github.com/tawasta/project",
    "author": "Futural",
    "license": "AGPL-3",
    "depends": [
        "hr_timesheet",
        "project_timesheet_time_control",
        "resource",
    ],
    "data": [
        "data/ir_cron.xml",
        "views/hr_employee_views.xml",
    ],
    "demo": [],
    "application": False,
    "installable": True,
}
