# -*- coding: utf-8 -*-
{
    'name': "xmarts_categoria",

    'summary': """
        Modelo para many o one en sale order""",

    'description': """

    """,

    'author': "Axel",
    'website': "",


    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/vistaCategoria.xml',
	'views/sale_order_line_xmarts.xml',
       
    ],
    # only loaded in demonstration mode
    'demo': [
        '',
    ],
}
