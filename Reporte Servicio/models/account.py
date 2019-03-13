from odoo import api, fields, models, _

class SaleOrder(models.Model):
    _inherit = 'account.invoice'

	Comentarioscob = fields.Text(string='Comentarioscob',readonly=0)
	Orden_de_compra= fields.Char(string='Orden de Compra',readonly=0)
