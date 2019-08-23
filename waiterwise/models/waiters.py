# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Waiters(models.Model):
    _name = "waiters"
    _description = "Waiters"
    _rec_name = "first_name"

    first_name = fields.Char(string="First Name", required=True, )
    last_name = fields.Char(string="Last Name", required=True, )
    email_address = fields.Char(string="Email Address", required=True, )
    phone_number = fields.Char(string="Phone Number", required=True, )
    id_number = fields.Char(string="ID Number", required=True, )
    dob = fields.Char(string="Date of Birth", required=True, )


class PotentialWaiters(models.Model):
    _name = "potential.waiters"
    _description = "Potential Waiters"

    first_name = fields.Char(string="First Name", required=True, )
    last_name = fields.Char(string="Last Name", required=True, )
    email_address = fields.Char(string="Email Address", required=True, )
    password = fields.Char(string="Password", required=True, )
    phone_number = fields.Char(string="Phone Number", required=True, )
    id_number = fields.Char(string="ID Number", required=True, )
    dob = fields.Char(string="Date of Birth", required=True, )
    cv = fields.Binary(string="CV", required=True, )

    @api.one
    def accept_waiter(self):
        x = self.env['res.users'].create({'name': self.first_name, 'email': self.email_address,
                                          'login': self.email_address, 'new_password': self.password})
        x.groups_id = self.env['res.groups'].search([("name", "=", "Waiter")])

        self.env['waiters'].create({'first_name': self.first_name, 'last_name': self.last_name, 'email_address': self.email_address,
                                    'phone_number': self.phone_number, 'id_number': self.id_number, 'dob': self.dob})

        self.env['potential.waiters'].search(
            [('email_address', '=', self.email_address)]).unlink()
