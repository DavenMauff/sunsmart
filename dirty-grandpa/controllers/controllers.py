# -*- coding: utf-8 -*-
from odoo import http

# class Dirty-grandpa(http.Controller):
#     @http.route('/dirty-grandpa/dirty-grandpa/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dirty-grandpa/dirty-grandpa/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dirty-grandpa.listing', {
#             'root': '/dirty-grandpa/dirty-grandpa',
#             'objects': http.request.env['dirty-grandpa.dirty-grandpa'].search([]),
#         })

#     @http.route('/dirty-grandpa/dirty-grandpa/objects/<model("dirty-grandpa.dirty-grandpa"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dirty-grandpa.object', {
#             'object': obj
#         })