# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Categorias(models.Model):
    _name = 'categorias'
    name = fields.Char()
    tipo = fields.Char()
    numero=fields.Integer()
