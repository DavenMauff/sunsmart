# -*- coding: utf-8 -*-
from odoo import http


class StudentApplication(http.Controller):
    @http.route('/application', auth='public')
    def index(self, **kw):
        return "Hello, world"
