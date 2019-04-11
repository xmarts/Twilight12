from odoo import api, fields, models, _

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    tasadecambio = fields.Float(related='currency_id.rate_ids.rate')
    cambio = fields.Float(string='Tipo de Cambio',digits=(12,3),compute='CalcularCambio',store=True)
   
    @api.depends('currency_id')
    def CalcularCambio(self):
        for record in self:
        	if (record.tasadecambio!=0):
        		record['cambio'] = 1/record.tasadecambio
    @api.multi
    def _prepare_invoice(self):
        res = super(SaleOrder, self)._prepare_invoice()
        res.update({
            'cambio':self.cambio,
            })
        return res


