from odoo import models, fields, api
from odoo.exceptions import ValidationError


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
    status = fields.Selection(
        [('confirm', 'Confirm'), ('approved', 'approved')], default="confirm")

    @api.constrains('id_number')
    def _check_length(self):
        if self.id_number != 13:
            raise ValidationError("Not a valid ID.")

    @api.constrains('phone_number')
    def _check_length(self):
        if self.phone_number != 10:
            raise ValidationError("Not a valid phone number.")

    @api.multi
    def add_em(self):
        x = self.env['res.users'].create(
            {'name': self.first_name, 'email': self.email_address, 'login': self.email_address, 'new_password': self.password})
        x.groups_id = self.env['res.groups'].search(
            [("name", "=", "Lecturer")])
        self.status = 'approved'
        # self.write.status = False

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
