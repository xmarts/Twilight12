# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Stock(models.Model):
    _inherit= 'categorias'
    Comentario = fields.Text(readonly=1)
    
