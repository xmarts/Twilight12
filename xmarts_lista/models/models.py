# -*- coding: utf-8 -*-

from odoo import models, fields, api

class XmartsLista(models.Model):
    _name = 'xmartslista'
    name = fields.Char()
    lastName = fields.Char()
    age=fields.Integer()
