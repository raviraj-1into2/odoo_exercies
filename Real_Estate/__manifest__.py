# -*- coding: utf-8 -*
{
    'name': 'Real Estate',
    'version': '1.0.2',
    'category': 'Estate',
    'sequence': -100,
    'summary': 'Real Estate',
    'description': """ show the real estate details """,
    'depends': [],
    'data': [
        'views/menu.xml',
        'views/property_view.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [],
    # 'installable':True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
