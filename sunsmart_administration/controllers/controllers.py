# -*- coding: utf-8 -*-
from odoo import http


class StudentApplication(http.Controller):
    @http.route('/portal', auth='public', )
    def index(self, **kw):
        return http.request.render('sunsmart_administration.index', {})
