from odoo import api, fields, models, tools, _

class product_pricelist(models.Model):
    _inherit = "product.pricelist"
    
    image_small = fields.Binary(attachment=True,related='currency_id.image_small',store=True)
    @api.multi
    def name_get(self):
    	return [(pricelist.id, '%s' % (pricelist.name)) for pricelist in self]
