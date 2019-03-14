# -*- coding: utf-8 -*-
from odoo import http

 class YourModuleName(http.Controller):
#   @http.route('/your_module_name/your_module_name/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/your_module_name/your_module_name/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('your_module_name.listing', {
#             'root': '/your_module_name/your_module_name',
#             'objects': http.request.env['your_module_name.your_module_name'].search([]),
#         })

#     @http.route('/your_module_name/your_module_name/objects/<model("your_module_name.your_module_name"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('your_module_name.object', {
#             'object': obj
#         })

    @http.route('/example/detail', type='http', auth='users', website=True)
    def navigate_to_detail_page(self):
	modelo = http.request.env['xmarts.Lista'].sudo().search([])
	return http.request.render('create_webpage_demo.detail_page', {'modelo':modelo})
