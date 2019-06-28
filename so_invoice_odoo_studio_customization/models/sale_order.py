from odoo import api, fields, models, _

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    #x_studio_field_QfxbS = fields.Many2one('res.partner',string='Project')
    
    @api.multi
    def _prepare_invoice(self):
        res = super(SaleOrder, self)._prepare_invoice()
        res.update({
            'project_id_from_so':self.x_studio_field_QfxbS.id,
            'x_studio_po_number':self.x_studio_po_number,
            })
        return res