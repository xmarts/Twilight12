from odoo import api, fields, models, _

class SaleSignature(models.Model):
    _inherit = 'sale.order.line'
    category = fields.Many2one('categorias',string='Categorias',readonly=0)

   
    


