from odoo import api, fields, models, _

class saleorder(models.Model):
	_inherit = 'sale.order'

	boton1=fields.Boolean()
	boton2=fields.Boolean()

	@api.onchange('boton2','boton1')
	def switch2(self):
		for record in self:
			record.boton1=!record.boton1
			record.boton2=!record.boton2
	








