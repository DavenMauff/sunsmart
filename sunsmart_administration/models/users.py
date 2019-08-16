from odoo import models, fields, api


class Users(models.Model):
    _name = 'users'
    _description = 'Users'
    _inherit = ['res.users']

    name = fields.Char(string="Name")
    email = fields.Char(string="Email")
    login = fields.Char(string="Login")
    new_password = fields.Char(string="Password")
