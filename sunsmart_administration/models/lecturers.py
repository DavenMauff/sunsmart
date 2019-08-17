from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Lecturers(models.Model):
    """
    A class used to represent a Degree

    ...

    Attributes
    ----------
    image : binary
        the profile picture of the lecturer

    first_name : str
        the first name of the lecturer

    last_name : str
        the last name of the lecturer

    email_address : str
        the email address of the lecturer

    phone_number : str
        the phone number of the lecturer

    id_number : str
        the id number of the lecturer

    department : str
        the department the lecturer is related to

    password : str
        the password used by the lecturer to login

    status : str
        the current status of the lecturer

    Methods
    -------
    _check_length(id_number)
        Checks the length of a ID number for verification

    _check_length(phone_number)
        Checks the length of a phone number for verification

    add_em(self)
        Adds the lecturer to the login users database, allocates them to lecturer group and updates status

    """

    _name = "lecturers"
    _description = 'Lecturers'
    _rec_name = "first_name"

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
        """Checks the length of a ID number for verification

        Parameters
        ----------
        id_number : str
            the lecturer ID number
        """
        if self.id_number != 13:
            raise ValidationError("Not a valid ID.")

    @api.constrains('phone_number')
    def _check_length(self):
        """Checks the length of a phone number for verification

        Parameters
        ----------
        phone_number : str
            the lecturer phone number
        """
        if self.phone_number != 10:
            raise ValidationError("Not a valid phone number.")

    @api.multi
    def add_em(self):
        """Adds the lecturer to the login users database, allocates them to lecturer group and updates status

        Parameters
        ----------
        self : str
            The lecturer details to satisfy the login users database
        """
        x = self.env['res.users'].create(
            {'name': self.first_name, 'email': self.email_address, 'login': self.email_address, 'new_password': self.password})
        x.groups_id = self.env['res.groups'].search(
            [("name", "=", "Lecturer")])
        self.status = 'approved'
