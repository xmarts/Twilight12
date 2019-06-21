from odoo import api, fields, models, tools, _

class sale_order(models.Model):
    _inherit = "sale.order"
    
    image_small = fields.Binary(attachment=True,related='currency_id.image_small',store=True)