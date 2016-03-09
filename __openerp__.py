# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: 
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
    'name': 'Project Customizations',
    'summary': 'Changes to Project app',
    'version': '8.0.0.1.6',
    'category': 'Project Management',
    'website': 'http://www.tawasta.fi',
    'author': 'Oy Tawasta Technologies Ltd.',
    'license': 'AGPL-3',
    'application': False,
    'installable': True,
    'depends': [
        'project_extension',
        'hr_timesheet_sheet',
        'hr_skill'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/project_form.xml',
        'views/project_tree.xml',
        'views/project_search.xml',
        'views/project_task_form.xml',
        'views/project_task_search.xml',
        'views/project_type.xml',
        'views/project_task_type.xml',
        'views/project_kanban.xml',
        'views/project_task_kanban.xml'
    ]
}