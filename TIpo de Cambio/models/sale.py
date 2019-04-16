from odoo import api, fields, models, _

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    tasadecambio = fields.Float(related='currency_id.rate_ids.rate')
    cambio = fields.Float(string='Tipo de Cambio Actual',digits=(12,3),compute='CalcularCambio',store=True,readonly=0,default='1')
    change=fields.Float(string="Tipo de cambio",related='currency_id.cambio',readonly=0,default='1')
    is_created_change=fields.Boolean(string="creado",store=True)
    
    
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
    @api.model
    def create(self, values):
        record = super(SaleOrder, self).create(values)
        dicts=self.env['res.currency'].sudo().search_read([],[('rate')])
        for item in dicts:
            if item['id'] == record.currency_id.id:
                tasa=float(item["rate"])
                x=1/tasa
                y=float(record.change)
                record[('is_created_change')]=True
                record[("cambio")]=y
                record[("change")]=x
                    
        return record
    @api.multi
    def write(self, vals):
        record = super(SaleOrder, self).write(vals)
        if vals.get('is_created_change', False):
            x=record.cambio
            vals[("cambio")]=x    
        return record


