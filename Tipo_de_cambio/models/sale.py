from odoo import api, fields, models, _

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    tasadecambio = fields.Float(related='currency_id.rate_ids.rate')
    cambio = fields.Float(string='Tipo de Cambio',digits=(12,3),compute='CalcularCambio',store=True,readonly=0,default='1')

    @api.onchange('currency_id')
    def CalcularCambio(self):
        for record in self:
            if record.tasadecambio!=0 and record.pricelist_id!=False:
                record['cambio'] = 1/record.tasadecambio
            else:
                pass

    @api.multi
    def _prepare_invoice(self):
        res = super(SaleOrder, self)._prepare_invoice()
        res.update({
            'cambio':self.cambio,
            })
        return res
   
    


