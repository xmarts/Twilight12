# -*- coding: utf-8 -*-
{
    'name': 'Xmarts Reporte Servicio ',
    'version': '11.0.3',
    'category': "",
    'description': """ Sales quotation Report 
    """,
    'author':'Axel ',
    'depends': ['base','sale_order_multi_lot_selection_v4','sale','purchase'],
    'data': [
	
	"reports/report_servicio.xml",
"reports/report_servicio_compra.xml",
"reports/reporte.xml",
	  
    ],
    'qweb': [
        ],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
}
