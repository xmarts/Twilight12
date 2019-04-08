# -*- coding: utf-8 -*-
{
    'name': "Sale Stock Extended",

    'summary': """
        Show Available qty and Reserved Qty Based on Configured Location """,

    'description': """ """,

    'category': 'Stock',
    'version': '0.1',

    'depends': ['sale_stock'],

    'data': [
        'wizard/res_config.xml',
        'views/sale_view.xml',
    ],
    'installable': True,
    'application': False,
}
