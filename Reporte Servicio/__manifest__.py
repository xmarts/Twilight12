# -*- coding: utf-8 -*-
{
    'name': "your_module_name",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','purchase','sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
      
	
	


	'reports/report_serv.xml',
	'reports/report_serv2.xml',
	

	
	
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
	"installable": True,
    	"auto_install": True,
}
