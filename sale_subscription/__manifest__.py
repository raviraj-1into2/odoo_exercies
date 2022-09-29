# -*- coding: utf-8 -*
{
    'name': 'Sale Subscription',
    'version': '2.0.1',
    'category': 'Sale',
    'sequence': -100,
    'summary': 'Sale Subscription management',
    'description': """ Sale Subscription management """,
    'depends': ['mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_sub.xml',
        'views/sale_sub_template.xml'
    ],
    'demo': [],
    # 'installable':True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
