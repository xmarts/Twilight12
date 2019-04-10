from odoo import api, fields, models, _

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'
    tasadecambio = fields.Float(related='currency_id.rate_ids.rate')
    cambiobill = fields.Float(string='Tipo de Cambio',digits=(12,3),compute='CalcularCambio',store=True)
   
    @api.depends('tasadecambio')
    def CalcularCambio(self):
        for record in self:
        	if (record.tasadecambio!=0):
        		record['cambiobill'] = 1/record.tasadecambio

    @api.multi
    def _prepare_invoice(self):
        res = super(PurchaseOrder, self)._prepare_invoice()
        res.update({
            'cambiobill':self.cambiobill,
            })
        return res

