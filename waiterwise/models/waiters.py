# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Waiters(models.Model):
    """
    A class used to represent (accepted) waiters

    ...

    Attributes
    ----------
    first_name : str
        the first name of the waiter

    last_name : str
        the last name of the waiter

    email_address : str
        the email address of the waiter

    phone_number : str
        the phone number of the waiter

    id_number : str
        the id number of the waiter

    dob : str
        the date-of-birth of the waiter
    """

    _name = "waiters"
    _description = "Waiters"
    _rec_name = "first_name"

    # Password is not kepy here for security reasons, and instead is stored in the encrypted res.users password field
    first_name = fields.Char(string="First Name", required=True, )
    last_name = fields.Char(string="Last Name", required=True, )
    email_address = fields.Char(string="Email Address", required=True, )
    phone_number = fields.Char(string="Phone Number", required=True, )
    id_number = fields.Char(string="ID Number", required=True, )
    dob = fields.Char(string="Date of Birth", required=True, )


class PotentialWaiters(models.Model):
    """
    A class used to represent potential waiters (applicants)

    ...

    Attributes
    ----------
    first_name : str
        the first name of the waiter

    last_name : str
        the last name of the waiter

    email_address : str
        the email address of the waiter

    password : str
        the password used by the waiter to login

    phone_number : str
        the phone number of the waiter

    id_number : str
        the id number of the waiter

    dob : str
        the date-of-birth of the waiter

    cv : binary
        the cv of the waiter

    Methods
    -------
    accept_waiter(self)
        Adds the waiter as an employee to the business. The waiter is moved from 'Potential Waiters' table to 'Waiters' table, and added 
        as a user to have login functionality. The waiter is also assigned to a group for security purposes, to only only read permissions 
        for the shift list. Waiter is also deleted from the 'Potential Waiters' table
    """

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

    # Button to accept waiter after they have applied to restuarant
    @api.one
    def accept_waiter(self):
        """Adds the waiter as an employee to the business. The waiter is moved from 'Potential Waiters' table to 'Waiters' table, and added 
        as a user to have login functionality. The waiter is also assigned to a group for security purposes, to only only read permissions 
        for the shift list. Waiter is also deleted from the 'Potential Waiters' table

        Parameters
        ----------
        self : str
            Waiter details from current table
        """
        # Once accepted, waiters are added to users so they're able to login and few shifts
        x = self.env['res.users'].create({'name': self.first_name, 'email': self.email_address,
                                          'login': self.email_address, 'new_password': self.password})
        # Waiters are also assigned groups so they're ONLY able to see the shift list, and they're not able to update it
        x.groups_id = self.env['res.groups'].search([("name", "=", "Waiter")])

        # Once waiters have been accepted and added to the database users, they will be moved to the 'Waiters' table
        self.env['waiters'].create({'first_name': self.first_name, 'last_name': self.last_name, 'email_address': self.email_address,
                                    'phone_number': self.phone_number, 'id_number': self.id_number, 'dob': self.dob})

        # Removes waiters from the 'Potential Waiters' table, becuase they're added to the 'Waiters' table
        self.env['potential.waiters'].search(
            [('email_address', '=', self.email_address)]).unlink()
