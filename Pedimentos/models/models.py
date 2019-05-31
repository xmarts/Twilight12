# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Pedimentos(models.Model):
    _name = 'pedimentos'
    _inherit = 'purchase.order'
   
    calib_id=fields.Integer()
