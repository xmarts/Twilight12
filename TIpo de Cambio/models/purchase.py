from odoo import api, fields, models, _

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'
    tasadecambio = fields.Float(related='currency_id.rate_ids.rate')

    cambiobill = fields.Float(string='Tipo de Cambio',digits=(12,3),compute='CalcularCambio',store=True,readonly=0)
    cambioq = fields.Float(string='Tipo de Cambio',digits=(12,3),compute='CalcularCambioi',store=True,readonly=0)
   
    @api.onchange('currency_id')
    def CalcularCambio(self):
        for record in self:
            if (record.tasadecambio!=0):
                record['cambiobill'] = 1/record.tasadecambio
            else:
                pass
    @api.onchange('cambiobill')
    def CalcularCambioi(self):
        for record in self:
            record['cambioq'] = record.cambiobill
            




