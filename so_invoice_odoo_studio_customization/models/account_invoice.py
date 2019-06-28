from odoo import api, fields, models, _

class AccountInvoice(models.Model):
    _inherit = 'account.invoice'
    
    project_id_from_so = fields.Many2one('res.partner',string='Project',readonly=1)
    x_studio_po_number = fields.Char(string='P.O. Number',readonly=1)
