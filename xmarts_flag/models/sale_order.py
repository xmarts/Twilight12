from odoo import api, fields, models, _

class saleorder(models.Model):
	_inherit = 'sale.order'

	boton1=fields.Boolean(default=True)
	boton2=fields.Boolean(default=False)

	@api.onchange('boton2','boton1')
	def switch2(self):
		self.boton1= not self.boton1
		self.boton2= not self.boton2
	









