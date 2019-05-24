from odoo import api, fields, models, _

class AccountInvoice(models.Model):
	_inherit = 'sale.order'
	
	credito_disponible = fields.Integer(string="Credito disponible" ,compute="_compute_credit")

	@api.onchange('partner_id')
	def _compute_credit(self):
		for record in self:
			x=self.env['res.partner'].sudo().search([('name','=',self.partner_id.name)]).credit_available
			record[("credito_disponible")]=x
			
	


