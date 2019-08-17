# -*- coding: utf-8 -*-
from odoo import http

# class Waiterwise(http.Controller):
#     @http.route('/waiterwise/waiterwise/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/waiterwise/waiterwise/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('waiterwise.listing', {
#             'root': '/waiterwise/waiterwise',
#             'objects': http.request.env['waiterwise.waiterwise'].search([]),
#         })

#     @http.route('/waiterwise/waiterwise/objects/<model("waiterwise.waiterwise"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('waiterwise.object', {
#             'object': obj
#         })