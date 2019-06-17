from odoo import api, fields, models, _

class SaleSignature(models.Model):
	_inherit = 'sale.order.line'
	product_uom_qty = fields.Float(default=2.0)
	








