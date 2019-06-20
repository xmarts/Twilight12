from odoo import api, fields, models, _	

class SaleOrder(models.Model):
	_inherit = 'sale.order'

	boton1=fields.Boolean(default=True,compute="switch2")
	boton2=fields.Boolean(default=False,compute="switch2")

	@api.onchange('boton2','boton1')
	def switch2(self):
		self.boton1= not self.boton1
		self.boton2= not self.boton2
	









