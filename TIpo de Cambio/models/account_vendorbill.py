from odoo import api, fields, models, _

class InvoiceCambio(models.Model):
    _inherit = 'account.invoice'
    tasadecambiobill = fields.Float(related='currency_id.rate_ids.rate')
    cambiobill = fields.Float(string='Tipo de Cambio',digits=(12,3),compute='CalcularCambio',store=True)
   
    @api.depends('tasadecambiobill')
    def CalcularCambio(self):
        for record in self:
        	if (record.cambiobill==0 and record.tasadecambiobill!=0):
        		record['cambiobill'] = 1/record.tasadecambiobill
        	else:
        		pass

   

