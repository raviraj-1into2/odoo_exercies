# -*- coding: utf-8 -*
{
    'name': 'Sale Order Delivery Status',
    'version': '1.0.0',
    'category': 'Order Delivery Status',
    'sequence': -100,
    'summary': 'delivery status of order',
    'description': """ show delivery status of order""",
    'depends': ['sale','sale_stock'],
    'data': [
        'views/sale_order_view.xml'
    ],
    'demo': [],
    # 'installable':True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
