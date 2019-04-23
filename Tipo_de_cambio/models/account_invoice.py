from odoo import api, fields, models, _

class InvoiceCambio(models.Model):
    _inherit = 'account.invoice'
    tasadecambio = fields.Float(related='currency_id.rate_ids.rate')
    cambio = fields.Float(string='Tipo de Cambio',compute='calcularcambio',digits=(12,3),store=True,readonly=0)

    @api.onchange('currency_id')
    def calcularcambio(self):
        for record in self:
            if (record.tasadecambio !=0):
                record['cambio'] = 1/record.tasadecambio
            else:
                pass

   

