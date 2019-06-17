from odoo import api, fields, models, _

class SaleSignature(models.Model):
	_inherit = 'sale.order.line'
	product_uom_qty = fields.Float(compute="_compute_change",store=True)
	@api.onchange("product_id")
	def _compute_change(self):
		for record in self:
			record[("product_uom_qty")]= 2








