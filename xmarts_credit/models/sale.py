from odoo import api, fields, models, _

class stockmovelinesp(models.Model):
	_inherit = 'stock.move.line'


	@api.onchange('product_id')
	def _compute_transito(self):
		for record in self:
			if record.done_move !=True and record.location_dest_id.id==13:
				producttemplate._compute_transito_product()


class producttemplate(models.Model):
	_inherit = 'product.template'

	cantidad_transito = fields.Char(string="cost" ,store=True,readonly=False)

	@api.onchange('product_id')
	def _compute_transito_product(self):
		for record in self:
			x = self.env['res.partner'].sudo().search([('product_id.id', '=', record.id)])
			record[("cantidad_transito")] = x


	


