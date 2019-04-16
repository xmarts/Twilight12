from odoo import api, fields, models, _

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'
    tasadecambio = fields.Float(related='currency_id.rate_ids.rate')

    cambiobill = fields.Float(string='Tipo de Cambio',digits=(12,3),compute='CalcularCambio',store=True)
   
    @api.depends('currency_id')
    def CalcularCambio(self):
        for record in self:
        	if (record.tasadecambio!=0 and record.state!="purchase"):
        		record['cambiobill'] = 1/record.tasadecambio



