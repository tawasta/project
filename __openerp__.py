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
    'category': 'Project',
    'version': '0.2',
    'author': 'Vizucom Oy',
    'website': 'http://www.vizucom.com',
    'depends': ['project'],
    'description': """
Project number field & generator
=========================================
* Retroactively generates project and tas numbers for all projects and tasks
* Starts from 10001, can be customized in data XML file
* Keeps track of assigned numbers internally, and gives a new one each time a new project or task is created
""",
    'data': [
        'view/project_form.xml',
        'view/project_tree.xml',
        'view/project_kanban.xml',
        'data/project_number_init.xml',
    ],
}
