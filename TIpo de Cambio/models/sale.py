from odoo import api, fields, models, _

class saleCambio(models.Model):
    _inherit = 'sale.order'
    TasadeCambio = fields.Float(related='currency_id.rate_ids.rate')
    Cambio = fields.Float(string='Tipo de Cambio',digits=(12,3),compute='CalcularCambio')
   
    @api.onchange('pricelist_id','TasadeCambio')
    def CalcularCambio(self):
        for record in self:
                record['Cambio'] = 1/record.TasadeCambio


