from odoo import api, fields, models, _

class InvoiceCambio(models.Model):
    _inherit = 'account.invoice'
    TasadeCambio = fields.Float(related='currency_id.rate_ids.rate')
    Cambio = fields.Float(string='Tipo de Cambio',digits=(12,3),compute='CalcularCambio')
   
    @api.onchange('currency_id','TasadeCambio')
    def CalcularCambio(self):
        for record in self:
                record['Cambio'] = 1/record.TasadeCambio


