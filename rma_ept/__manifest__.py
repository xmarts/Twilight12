{
   
    # App information
    'name': 'RMA ( Return Merchandise Authorization ) in Odoo',
    'version': '12.0',
    'category': 'Sales',
    'license': 'OPL-1',
    'summary' : 'Manage Return Merchandize Authorization ( RMA ) in Odoo. Allow users to manage Return Orders, Replacement, Refund & Repair in Odoo.',
    
    # Author
    'author': 'Emipro Technologies Pvt. Ltd.',
    'maintainer': 'Emipro Technologies Pvt. Ltd.',   
    'website': 'http://www.emiprotechnologies.com/',
    
    # Dependencies
    'depends': ['delivery','crm'],
    
    
    'data': [
                'data/rma_reason_ept.xml',
                'security/res_groups.xml',
                'report/rma_report.xml',
                'report/rma_report_template.xml',
                'views/mail_template_data.xml',
                'views/crm_claim_ept_sequence.xml',
                'views/view_account_invoice.xml',
                'wizard/view_claim_process_wizard.xml',
                'views/crm_claim_ept_view.xml',
                'views/view_stock_picking.xml',
                'views/rma_reason_ept.xml',
                'views/view_stock_warehouse.xml',
                'views/sale_order_view.xml',
                'security/ir.model.access.csv',
             ],
             
	# Odoo Store Specific   
    'images': ['static/description/RMA__Odoo_Covor.jpg'],

             
     # Technical        
    
    'installable': True,
    'auto_install': False,
    'application' : True,
    'active': False,
    'price': 249.00,
    'live_test_url':'https://www.emiprotechnologies.com/free-trial?app=rma-ept&version=12&edition=enterprise',
    'currency': 'EUR',          
             
  
}
