# -*- coding: utf-8 -*-
from odoo import http

# class MyodooWarning(http.Controller):
#     @http.route('/myodoo_warning/myodoo_warning/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/myodoo_warning/myodoo_warning/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('myodoo_warning.listing', {
#             'root': '/myodoo_warning/myodoo_warning',
#             'objects': http.request.env['myodoo_warning.myodoo_warning'].search([]),
#         })

#     @http.route('/myodoo_warning/myodoo_warning/objects/<model("myodoo_warning.myodoo_warning"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('myodoo_warning.object', {
#             'object': obj
#         })