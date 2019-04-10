from odoo import api, fields, models, _

class InvoiceCambio(models.Model):
    _inherit = 'account.invoice'
    tasadecambio = fields.Float(related='currency_id.rate_ids.rate')
    cambio = fields.Float(string='Tipo de Cambio',digits=(12,3),compute='CalcularCambio',store=True)
   
    @api.depends('tasadecambio')
    def CalcularCambio(self):
        for record in self:
        	if (record.cambio==0 and record.tasadecambio!=0):
        		record['cambio'] = 1/record.tasadecambio
        	else:
        		pass

   

