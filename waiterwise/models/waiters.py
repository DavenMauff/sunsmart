# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PotentialWaiters(models.Model):
    _name = "potential.waiters"
    _description = "Potential Waiters"

    first_name = fields.Char(string="First Name", required=True, )
    last_name = fields.Char(string="Last Name", required=True, )
    phone_number = fields.Char(string="Phone Number", required=True, )
    id_number = fields.Char(string="ID Number", required=True, )
    dob = fields.Char(string="Date of Birth", required=True, )
