from odoo import api, fields, models, _

class ACCorder(models.Model):
    _inherit = 'account.invoice'
    
    Comentarioscob = fields.Text(string='Comentarioscob')
    Orden_de_compra= fields.Char(string='Orden de Compra')
