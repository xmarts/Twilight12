{
    'name': 'Xmarts Tipo de Cambio ',
    'version': '11.0.3',
    'category': "",
    'description': """ get data from currency_id 
    """,
    'author':'Axel indian God',
    'depends': ['account','sale','account_accountant'],
    'data': [
	'views/sale_order_view.xml',
	'views/invoice_view.xml',
	'views/invoice_view_bill.xml',
	'views/purchase_order_view .xml',

	'report/reporte_invoice.xml',
	'report/reporte_sale.xml',
	  
    ],
    'qweb': [
        ],

    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
}
