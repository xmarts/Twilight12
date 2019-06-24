from odoo import api, fields, models, _

class stockmovelinesp(models.Model):
    _inherit = 'stock.move.line'

    @api.onchange('product_id')
    def _compute_transito(self):
        for record in self:
            if record.done_move !=True and record.location_dest_id.id==13:
                x=self.env['product.template']
                x._compute_transito_product(self)



class Product_template(models.Model):
    _inherit = 'product.template'

    cantidad_transito = fields.Char(string="cost" ,store=True,readonly=False)
    @api.multi
    def _compute_transito_product(self):
        for record in self:
            x = self.env['stock.move.line'].sudo().search([('product_id', '=', record.id)])
            record[("cantidad_transito")] = 21
