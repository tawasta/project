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
    'name': 'Project Modifications',
    'description': """

Task notes and project button.

    """,
    'version': '8.0.0.1.2',
    'category': 'Project Management',
    'website': 'http://www.tawasta.fi',
    'author': 'Oy Tawasta Technologies Ltd.',
    'license': 'AGPL-3',
    'depends': [ 
        'project'
    ],
    'data': [
        'views/project_form.xml',
        'views/project_note.xml',
        'views/task_form.xml',
        'views/task_note.xml',
        'views/res_partner.xml',
        'views/project.xml',
        'views/project_kanban.xml',
        'security/ir.model.access.csv'
    ],
    'installable': True,
    'auto-install': False,
    
}
