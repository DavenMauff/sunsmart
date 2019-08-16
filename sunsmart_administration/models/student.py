from odoo import models, fields, api


class Students(models.Model):
    _name = "students"
    _description = "Students"
    _rec_name = "first_name"

    userid = fields.Char(string='userid', )
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

    @api.one
    def accept_student(self):
        x = self.env['res.users'].create(
            {'name': self.first_name, 'email': self.email_address, 'login': self.email_address, 'new_password': self.password})
        y = x
        x.groups_id = self.env['res.groups'].search(
            [("name", "=", "Student")])
        self.env['students'].create({'profile_picture': self.profile_picture, 'first_name': self.first_name, 'last_name': self.last_name,
                                     'email_address': self.email_address, 'id_number': self.id_number, 'dob': self.dob, 'degree_choice': self.degree_choice.degree_name, 'userid': y.id})

        modules = [self.degree_choice.module_1.module_name, self.degree_choice.module_2.module_name, self.degree_choice.module_3.module_name, self.degree_choice.module_4.module_name, self.degree_choice.module_5.module_name, self.degree_choice.module_6.module_name,
                   self.degree_choice.module_7.module_name, self.degree_choice.module_8.module_name, self.degree_choice.module_9.module_name, self.degree_choice.module_10.module_name, self.degree_choice.module_11.module_name, self.degree_choice.module_12.module_name]
        departments = [self.degree_choice.module_1.lecturer.department.department_name, self.degree_choice.module_2.lecturer.department.department_name, self.degree_choice.module_3.lecturer.department.department_name, self.degree_choice.module_4.lecturer.department.department_name, self.degree_choice.module_5.lecturer.department.department_name, self.degree_choice.module_6.lecturer.department.department_name,
                       self.degree_choice.module_7.lecturer.department.department_name, self.degree_choice.module_8.lecturer.department.department_name, self.degree_choice.module_9.lecturer.department.department_name, self.degree_choice.module_10.lecturer.department.department_name, self.degree_choice.module_11.lecturer.department.department_name, self.degree_choice.module_12.lecturer.department.department_name]

        for x in range(12):
            student_module = modules[x]
            department = departments[x]
            self.env['marks'].create({'userid': y.id, 'student_id_number': self.id_number, 'student_email': self.email_address, 'student_first_name': self.first_name,
                                      'student_last_name': self.last_name, 'department': department, 'module': student_module, 'result': 0})

        # for x in range(11):
        #     temp = "degree_choice.module_" + str(x)
        #     student_module = self + '.' + temp
        #     department = self + '.' + temp.lecturers.department
        #     self.env['marks'].create({'student_id_number': self.id_number, 'student_first_name': self.first_name,
        #                               'student_last_name': self.last_name, 'department': department, 'module': student_module, 'result': 0})

        # for x in range(0, len(self.degree_choice.module_name)):
        #     student_module = self.degree_choice.module_name[x].name
        #     department = self.degree_choice.module_name[x].department_name.name
        #     self.env['marks'].create({'student_id_number': self.id_number, 'student_first_name': self.first_name,
        #                               'student_last_name': self.last_name, 'department': department, 'module': student_module, 'result': 0})

        self.env['student.application'].search(
            [('email_address', '=', self.email_address)]).unlink()
        # for loop to add the student multiple times for each module
