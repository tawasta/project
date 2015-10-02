{
    'name': 'Report-module',
    'description': """

Module for presenting reports of projectmodule.

    """,
    
    'author': 'Aleksi Savijoki',
    'depends': ['project', 'web_graph_improved'],
    'version': '1.0',
    'data': [ 
    	'views/project_project_view.xml', 
    	'views/project_report_view.xml',
    	'views/project_report_qweb.xml',
    	'security/ir.model.access.csv'
    ],
    'installable': True,
    'auto-install': False,
    
}
