from odoo import api, fields, models, _

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    
    @api.onchange('partner_id')
    def onchange_partner_id(self):
        self.email = self.partner_id.email
        self.phone = self.partner_id.phone
        
    @api.onchange('email','phone')
    def onchange_phone_email(self):
        if self.partner_id:
            self.partner_id.write({'email': self.email,'phone':self.phone})
    