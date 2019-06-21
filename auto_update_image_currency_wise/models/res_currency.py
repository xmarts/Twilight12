from odoo import api, fields, models, tools, _

class res_currency(models.Model):
    _inherit = "res.currency"
    
    image_small = fields.Binary(attachment=True)