# -*- coding: utf-8 -*-
##############################################################################
#
#   Copyright (c) 2013- Vizucom Oy (http://www.vizucom.com)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Project number generator',
    'summary': 'Adds notes for project and task. DEPRECATED',
    'version': '8.0.1.0.0',
    'category': 'Project Management',
    'website': 'https://github.com/Tawasta/project',
    'author': 'Vizucom Oy',
    'license': 'AGPL-3',
    'depends': [
        'project'
    ],
    'data': [
        'view/project_form.xml',
        'view/project_tree.xml',
        'view/project_kanban.xml',
        'view/project_search.xml',
        'view/task_form.xml',
        'view/task_tree.xml',
        'view/task_kanban.xml',
        'view/task_search.xml',
        'data/project_number_init.xml',
        'data/task_number_init.xml',
    ],
    'installable': False,
    'auto-install': False,

}
