from odoo import api, fields, models, _


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    lot_ids = fields.Many2many('stock.production.lot',string='Lot', copy=False)
    
    @api.onchange('lot_ids')
    def onchange_lot(self):
        self.product_uom_qty = 0.0
        for lot in self.lot_ids:
            self.product_uom_qty += lot.product_qty 
            
    @api.multi
    def _prepare_invoice_line(self, qty):
        res = super(SaleOrderLine, self)._prepare_invoice_line(qty)        
        if self.lot_ids:            
            res.update({'lot_ids' : [(6, 0, self.lot_ids.ids)]})
        return res

    @api.multi
    @api.onchange('product_id')
    def product_id_change(self):
        result = super(SaleOrderLine, self).product_id_change()
        lot_id = self.env['stock.production.lot'].search([('product_id', '=', self.product_id.id),('product_qty','=',0.0)])
        lot = lot_id.filtered(lambda lot:lot.product_qty > 0 and lot.product_id.id == self.product_id.id)
        result['domain'].update({'lot_ids': [('id', 'in', lot.ids)]})
        return result
