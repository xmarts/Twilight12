from odoo import api, fields, models, _

class SaleSignature(models.Model):
    _inherit = 'res.users'
    signatureSale = fields.Html(string='Firma ventas')

   
    


