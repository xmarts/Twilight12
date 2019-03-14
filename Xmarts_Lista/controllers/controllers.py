# -*- coding: utf-8 -*-
from odoo import http

class YourModuleName(http.Controller):
	@http.route('/example/detail', type='http', auth='users', website=True)
	def navigate_to_detail_page(self):
		modelo = http.request.env['xmarts.Lista'].sudo().search([])
		return http.request.render('create_webpage_demo.detail_page', {'modelo':modelo})
