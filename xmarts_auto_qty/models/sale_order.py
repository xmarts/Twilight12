from odoo import api, fields, models, _

class SaleSignature(models.Model):
	_inherit = 'sale.order.line'
	def get_sale_order_line_multiline_description_sale(self, product):

		return "PRUEBA"
	








