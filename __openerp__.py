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
    'name': 'Project Reports',
    'description': """

Module for presenting reports of project-module.

    """,
    'version': '8.0.0.2.1',
    'category': 'Project Management',
    'website': 'http://www.tawasta.fi',
    'author': 'Oy Tawasta Technologies Ltd.',
    'license': 'AGPL-3',
    'depends': [ 
        'web_graph_improved', 
        'hr', 
        'analytic_contract_hr_expense',
        'project_customizations'
    ],
    'data': [ 
    	# 'views/project_project_view.xml', 
    	# 'views/project_report_view.xml',
    	# 'views/project_report_qweb.xml',
     #    'views/hr_employee_view.xml',
    	'security/ir.model.access.csv',
        'views/project_task_report.xml'
    ],
    'installable': True,
    'auto-install': False,
    
}
