# -*- encoding: utf-8 -*-
# Part of Adquat Solutions. See LICENSE file for full copyright and licensing details.

# Copyright (c) 2011 Adquat Solutions - SARL (http://adquat.com).

{
    'name' : 'Adquat Account Grouped',
    'category': 'Accounting',
    'summary': """
    Create grouped account move line view (useful to export grouped expense and income pieces lines)
    """,
    'price' : 10.00,
    'currency' : 'EUR',
    'author': "adquat-solutions",
    'website': 'http://www.adquat.com',
    'depends' : ['account'],
    'data': [
        'security/ir.model.access.csv',
        'account_view.xml',
        ],
    'installable': True,
    'application': False,
}