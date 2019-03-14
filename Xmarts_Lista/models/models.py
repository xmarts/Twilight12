# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Xmarts_Lista(models.Model):
	_name = 'xmarts.Lista'

	name = fields.Char()
	value = fields.Integer()
	description = fields.Text()


