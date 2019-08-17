from odoo import models, fields, api


class Users(models.Model):
    """
    A class used to represent all Users that may login, however is for testing purpose

    ...

    Attributes
    ----------
    name : str
        the name of the user

    email : str
        the email address of the user

    login : str
        the unique login of the user

    new_password : str
        the password of the user
    """
    _name = 'users'
    _description = 'Users'
    _inherit = ['res.users']

    name = fields.Char(string="Name")
    email = fields.Char(string="Email")
    login = fields.Char(string="Login")
    new_password = fields.Char(string="Password")
