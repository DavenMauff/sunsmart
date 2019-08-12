# -*- coding: utf-8 -*-
from odoo import http

# class SunsmartAdministration(http.Controller):
#     @http.route('/sunsmart_administration/sunsmart_administration/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sunsmart_administration/sunsmart_administration/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sunsmart_administration.listing', {
#             'root': '/sunsmart_administration/sunsmart_administration',
#             'objects': http.request.env['sunsmart_administration.sunsmart_administration'].search([]),
#         })

#     @http.route('/sunsmart_administration/sunsmart_administration/objects/<model("sunsmart_administration.sunsmart_administration"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sunsmart_administration.object', {
#             'object': obj
#         })