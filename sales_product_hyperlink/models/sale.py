# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    product_link = fields.Char(string="Link", copy=False)

    @api.model
    def create(self, vals):
        res = super(SaleOrderLine, self).create(vals)
        if res.product_id and res.product_id.product_link:
            res.product_link = res.product_id.product_link
        return res

    @api.multi
    def write(self, vals):
        if vals.get('product_id'):
            product_id = self.env['product.product'].browse(vals['product_id'])
            if product_id and product_id.product_link:
                vals.update({'product_link': product_id.product_link})
        return super(SaleOrderLine, self).write(vals)

    @api.multi
    @api.onchange('product_id')
    def product_id_change(self):
        res = super(SaleOrderLine, self).product_id_change()
        self.product_link = ''
        if self.product_id:
            self.product_link = self.product_id.product_link
        return res

    @api.multi
    def open_link(self):
        if self.product_link:
            return {
                  'name'     : 'Open',
                  'res_model': 'ir.actions.act_url',
                  'type'     : 'ir.actions.act_url',
                  'target'   : 'new',
                  'url'      : self.product_link
               }