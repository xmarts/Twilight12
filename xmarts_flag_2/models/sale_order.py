from odoo import api, fields, models, _	

class Pricelist(models.Model):
	_inherit = 'product.pricelist'

	@api.multi
	def name_get(self):
		return [(pricelist.id, '%s' % (pricelist.name)) for pricelist in self]








