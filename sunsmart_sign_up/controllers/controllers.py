# -*- coding: utf-8 -*-
from odoo import http

# class SunsmartSignUp(http.Controller):
#     @http.route('/sunsmart_sign_up/sunsmart_sign_up/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sunsmart_sign_up/sunsmart_sign_up/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sunsmart_sign_up.listing', {
#             'root': '/sunsmart_sign_up/sunsmart_sign_up',
#             'objects': http.request.env['sunsmart_sign_up.sunsmart_sign_up'].search([]),
#         })

#     @http.route('/sunsmart_sign_up/sunsmart_sign_up/objects/<model("sunsmart_sign_up.sunsmart_sign_up"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sunsmart_sign_up.object', {
#             'object': obj
#         })