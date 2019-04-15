from odoo import api, fields, models, _

class SaleOrderC(models.Model):
    _inherit = 'res.currency'
    cambio = fields.Float(string='Tasa Comercial',digits=(12,3),compute='CalcularCambio',store=True,readonly=0)
   
    @api.depends('rate')
    def CalcularCambio(self):
        for record in self:
        	if (record.rate!=0):
        		record['cambio'] = 1/record.rate
 


