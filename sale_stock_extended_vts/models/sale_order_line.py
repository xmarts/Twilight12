
from odoo import api, models,fields
from odoo.addons import decimal_precision as dp

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"
    
    @api.multi
    @api.depends('product_id','qty_delivered')
    def _compute_available_reserved_qty(self):
        for order_line in self:
            params = self.env['ir.config_parameter'].sudo()
            location_id = params.get_param('sale_stock_extended_vts.stock_location_id')
            if isinstance(location_id,str):
                location_id = int(location_id)
            if order_line.product_id and location_id:
                #order_line.qty_available = order_line.product_id.with_context(location=location_id).qty_available
                order_line.qty_available = sum(self.env['stock.quant'].sudo().search([('location_id','=',location_id),('product_id','=',order_line.product_id.id)]).sudo().mapped('quantity'))
                order_line.reserved_product_qty = sum(self.env['stock.quant'].sudo().search([('location_id','=',location_id),('product_id','=',order_line.product_id.id)]).sudo().mapped('reserved_quantity'))
                
    qty_available = fields.Float(string='Available Qty',copy=False, compute='_compute_available_reserved_qty',compute_sudo=True, store=True, digits=dp.get_precision('Product Unit of Measure'))
    reserved_product_qty = fields.Float(string='Reserved Qty',copy=False,compute='_compute_available_reserved_qty',compute_sudo=True, store=True, digits=dp.get_precision('Product Unit of Measure'))
    