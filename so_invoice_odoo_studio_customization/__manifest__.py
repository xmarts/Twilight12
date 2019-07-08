{
    'name': 'Sale Invoice Odoo Studio Customization',
    'version': '11.0.3',
    'category': 'Sales Management',
    'description': """ get data from sale order and set in the Invoice.
    """,
    'author':'Vraja Technologies',
    'depends': ['sale','account'],
    'data': [
          'view/account_invoice.xml',
    ],
    'qweb': [
        ],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
}
