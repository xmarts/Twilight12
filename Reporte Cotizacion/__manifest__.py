{
    'name': 'Xmarts Reporte cotizacion ',
    'version': '11.0.3',
    'category': "",
    'description': """ Sales quotation Report 
    """,
    'author':'Axel',
    'depends': ['base','sale'],
    'data': [
	
	"views/Sale_signature.xml",
	"report/sale_order_report.xml",
	  
    ],
    'qweb': [
        ],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
    "images":['static/src/img/banco.png','static/src/img/sello.png'],
}
