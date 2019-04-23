# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Oy Tawasta OS Technologies Ltd.
#    Copyright 2015 Oy Tawasta OS Technologies Ltd. (http://www.tawasta.fi)
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
    'name': 'Project and task types and skills',
    'summary': 'Adds types for tasks and projects and skills for tasks',
    'version': '1.0.0',
    'category': 'Project Management',
    'website': 'https://github.com/Tawasta/project',
    'author': 'Oy Tawasta Technologies Ltd.',
    'license': 'AGPL-3',
    'application': False,
    'installable': True,
    'depends': [
        'hr_skill',
        'hr_timesheet_sheet',
    ],
    'data': [
        'security/ir.model.access.csv',

        'views/project_form.xml',
        'views/project_kanban.xml',
        'views/project_search.xml',

        'views/project_task_class.xml',
        'views/project_task_form.xml',
        'views/project_task_kanban.xml',
        'views/project_task_search.xml',

        'views/project_tree.xml',
        'views/project_type.xml',
    ]
}
