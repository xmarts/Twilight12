# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    x_link = fields.Char(string="Link", copy=False, related='product_template.x_link')