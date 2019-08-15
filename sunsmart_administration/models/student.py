from odoo import models, fields, api


class Students(models.Model):
    _name = "students"
    _description = "Students"
    _rec_name = "first_name"

    profile_picture = fields.Binary(string="Profile Picture", )
    first_name = fields.Char(string="First Name", required=True, )
    last_name = fields.Char(string="Last Name", required=True, )
    email_address = fields.Char(string='Email Address', required=True, )
    id_number = fields.Char(string="ID Number", required=True, )
    dob = fields.Date(string="Date-of-Birth", required=True, )
    degree_choice = fields.Char(string="Degree", required=True, )


class StudentApplication(models.Model):
    _name = "student.application"
    _description = "Student Application"

    profile_picture = fields.Binary(string="Profile Picture", )
    first_name = fields.Char(string="First Name", required=True, )
    last_name = fields.Char(string="Last Name", required=True, )
    email_address = fields.Char(string='Email Address', required=True, )
    password = fields.Char(string="Password", required=True, )
    id_number = fields.Char(string="ID Number", required=True, )
    dob = fields.Date(string="Date-of-Birth", required=True, )
    degree_choice = fields.Many2one(
        'degrees', string="Degree Choice", required=True, )
    transcripts = fields.Binary(string="Upload Transcripts", required=True, )

    @api.multi
    def accept_student(self):
        x = self.env['res.users'].create(
            {'name': self.first_name, 'email': self.email_address, 'login': self.email_address, 'new_password': self.password})

        self.env['students'].create({'profile_picture': self.profile_picture, 'first_name': self.first_name, 'last_name': self.last_name,
                                     'email_address': self.email_address, 'id_number': self.id_number, 'dob': self.dob, 'degree_choice': self.degree_choice.degree_name})
        self.env['student.application'].search(
            [('email_address', '=', self.email_address)]).unlink()
