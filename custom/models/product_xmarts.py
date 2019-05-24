from odoo import api, fields, models, _

class productT(models.Model):
    _inherit = 'product.template'
    
    x_link = fields.Char(string='Link')
    
 
