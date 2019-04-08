from odoo import models,fields,api,_
from odoo.exceptions import Warning
import logging
_logger = logging.getLogger(__name__)


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    stock_location_id = fields.Many2one('stock.location',string="Location")

    @api.multi
    def set_values(self):
        super(ResConfigSettings, self).set_values()
        Param = self.env['ir.config_parameter'].sudo()
        Param.set_param("sale_stock_extended_vts.stock_location_id", (self.stock_location_id.id or False))

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        params = self.env['ir.config_parameter'].sudo()
        stock_location_id = params.get_param('sale_stock_extended_vts.stock_location_id', default=False)
        stock_location=stock_location_id and self.env['stock.location'].search([('id','=',stock_location_id)]) or False
        res.update(stock_location_id=stock_location and stock_location.id or False)
        return res
