from odoo import api, fields, models, _	

class SaleOrder(models.Model):
	_inherit = 'sale.order'

	boton1=fields.Boolean(default=True,compute="switch2",readonly=0)
	boton2=fields.Boolean(default=False,compute="switch2",readonly=0)

	@api.onchange('boton2','boton1')
	def switch2(self):
		for record in self:

			record[("boton1")]= not record.boton1
			record[("boton2")]= not record.boton2
	









