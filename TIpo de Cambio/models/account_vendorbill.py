from odoo import api, fields, models, _

class InvoiceCambio(models.Model):
    _inherit = 'account.invoice'
    tasadecambiobill = fields.Float(related='currency_id.rate_ids.rate')
    cambiobill = fields.Float(string='Tipo de Cambio',digits=(12,3),store=True)


    @api.onchange('currency_id')
    def calcularcambio2(self):
        for record in self:
        	if (record.tasadecambiobill!=0):
        		record['cambiobill'] = 1/record.tasadecambiobill
        	else:
        		pass
    
   

