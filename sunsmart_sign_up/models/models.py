# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StudentRegistration(models.Model):
    _name = "student.registration"  # table name in DB
    _description = "Student Registration"

   # TODO: Link degree field with table in adinistration module
   # Install mobile verification module for phone number field
   # Add generic email to forward student number to
   # Create dropdown for degrees
    student_number = fields.Integer(
        string='SST', default=lambda self: self.env['ir.sequence'].next_by_code('increment_student_number'))
    first_name = fields.Char(string='First Name', required=True, )
    last_name = fields.Char(string='Last Name', required=True, )
    phone_number = fields.Integer(string='Phone Number', required=True, )
    degree = fields.Many2one(comodel_name='', string='degree', required=True, )
    id_number = fields.Char(string='ID Number', required=True, )
    upload_file = fields.Binary(string="Upload File", required=True, )
    file_name = fields.Char(string="File Name", required=True, )
