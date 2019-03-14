# -*- coding: utf-8 -*-
from odoo import http

class MyfirstModel(http.Controller):
    @http.route('/stock/categorias', type='http', auth='public', website=True)
    def render_example_page(self):
        categorias = http.request.env['Categorias'].sudo().search([])
        return http.request.render('myfirst_model.vistaCategoria',{'Categorias':categorias})


