from odoo import api, fields, models, _

class SaleSignature(models.Model):
	_inherit = 'sale.order.line'
	def get_sale_order_line_multiline_description_sale(self, product):
		result=self.product_id.default_code +" "+ self.product_id.name

		return result
	








