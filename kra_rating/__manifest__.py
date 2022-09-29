# -*- coding: utf-8 -*
{
    'name': 'Kra Rating',
    'version': '1.0.0',
    'category': 'Rating',
    'sequence': -100,
    'summary': 'Kra Rating management',
    'description': """ Manage the employee rating """,
    'depends': ['sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/year_view.xml',
        'views/kra_view.xml',
        'views/question_view.xml',
        'views/res_partner_view.xml',
        'views/customers_view.xml'
    ],
    'demo': [],
    # 'installable':True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
