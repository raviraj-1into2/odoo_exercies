# -*- coding: utf-8 -*
{
    'name': 'Project Management',
    'version': '1.0.0',
    'category': 'Project',
    'sequence': -100,
    'summary': 'Project Management',
    'description': """ Manage the employee timesheet and project""",
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/project_view.xml',
    ],
    'demo': [],
    # 'installable':True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
