
# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Users(models.Model):
    _name = 'users'
    _description = 'Users'
    _inherit = ['res.users']

    name = fields.Char(string="Name")
    email = fields.Char(string="Email")
    login = fields.Char(string="Login")
    new_password = fields.Char(string="Password")


class Departments(models.Model):
    _name = 'departments'
    _description = 'Departments'
    _rec_name = 'department_name'

    department_name = fields.Char(string="Department Name", required=True, )


class Lecturers(models.Model):
    _name = "lecturers"
    _description = 'Lecturers'
    _rec_name = "first_name"
    # _inherit = ['res.users']

    image = fields.Binary("Image", help="Select image here", store=True)
    first_name = fields.Char(string="First Name", required=True, )
    last_name = fields.Char(string="Last Name", required=True, )
    email_address = fields.Char(string="Email Address", required=True)
    phone_number = fields.Char(string="Phone Number", required=True, )
    id_number = fields.Char(string="ID Number", required=True, )
    department = fields.Many2one(
        comodel_name='departments', )
    password = fields.Char(String="password", required=True,)
    status = fields.Boolean(string='status', default=True, )

    @api.multi
    def add_em(self):
        x = self.env['res.users'].create(
            {'name': self.first_name, 'email': self.email_address, 'login': self.email_address, 'new_password': self.password})
        # self.write.status = False
        self.write({'status': False})
        # data = {'value': {'status': 'approve'}}
        # return data

        # @api.multi
        # def add_lecturer(self):
        #     x = self.env['res.users'].create(
        #         {'name': self.first_name, 'email': self.login, 'login': self.login, 'new_password': self.password})

        # @api.model
        # def create(self, cr, uid, vals, context=None):
        #     user_obj = self.pool.get('res.users')
        #     vals_user = {
        #         'name': vals.get('first_name'),
        #         'login': 'default_login',
        #         'password': 'password'
        #     }
        #     user_obj.create(cr, uid, vals_user, context)
        #     result = super(hr_employee, self).create(
        #         cr, uid, vals, context=context)
        #     return result

        # @api.model
        # def create(self, vals):
        #     user_vals = {
        #         'name': vals.get('first_name'),
        #         'login': 'login@gmail.com',
        #         'password': 'password',
        #     }
        #     user_id = self.env['res.users'].create(user_vals)
        #     return super(Lecturers, self).create(vals)

        # @api.model
        # def create(self, vals):
        #     res = super(Lecturers, self).create(vals)
        #     self.env['res.users'].create({
        #         'user': vals['login'],
        #         'email': vals['login'],
        #         'login': vals['login'],
        #         'new_password': vals['password']
        #     })
        #     res = super(Lecturers, self).create(vals)
        #     return res


class Modules(models.Model):
    _name = 'modules'
    _description = 'Modules'
    _rec_name = 'module_name'

    module_name = fields.Char(string="Module Name", required=True, )
    lecturer = fields.Many2one(comodel_name='lecturers',)


class Degree(models.Model):
    _name = 'degrees'
    _description = 'Degrees'
    _rec_name = 'degree_name'

    name = fields.Char(compute="_get_degree_name")
    degree_name = fields.Char(string="Degree Name", required=True, )
    module_1 = fields.Many2one(comodel_name='modules', )
    module_2 = fields.Many2one(comodel_name='modules', )
    module_3 = fields.Many2one(comodel_name='modules', )
    module_4 = fields.Many2one(comodel_name='modules', )
    module_5 = fields.Many2one(comodel_name='modules', )
    module_6 = fields.Many2one(comodel_name='modules', )
    module_7 = fields.Many2one(comodel_name='modules', )
    module_8 = fields.Many2one(comodel_name='modules', )
    module_9 = fields.Many2one(comodel_name='modules', )
    module_10 = fields.Many2one(comodel_name='modules', )
    module_11 = fields.Many2one(comodel_name='modules', )
    module_12 = fields.Many2one(comodel_name='modules', )

    @api.multi
    def _get_degree_name(self):
        for record in self:
            record.name = record.degree_name
