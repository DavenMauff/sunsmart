from odoo import models, fields, api


class StudentApplication(models.Model):
    _name = "student.application"
    _description = "Student Application"

    profile_picture = fields.Binary(string="Profile Picture", )
    first_name = fields.Char(string="First Name", required=True, )
    last_name = fields.Char(string="Last Name", required=True, )
    id_number = fields.Char(string="ID Number", required=True, )
    dob = fields.Date(string="Date-of-Birth", required=True, )
    degree_choice = fields.Many2one(
        comodel_name='degrees', string="Degree Choice", required=True, )
    transcripts = fields.Binary(string="Upload Transcripts", required=True, )
