from odoo import models, fields, api


class Students(models.Model):
    """
    A class used to represent accepted Students

    ...

    Attributes
    ----------
    userid : str
        the unique user id assosiated with the student login database

    profile_picture : binary
        the profile picture of the student

    first_name : str
        the first name of the student

    last_name : str
        the last name of the student

    email_address : str
        the email address of the student

    id_number : str
        the id number of the student

    dob : date
        the date of birth of the student

    degree_choice : str
        the degree choice of the student
    """

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
    """
    A class used to represent a potential students

    ...

    Attributes
    ----------
    profile_picture : binary
        the profile picture of the student

    first_name : str
        the first name of the student

    last_name : str
        the last name of the student

    email_address : str
        the email address of the student

    id_number : str
        the id number of the student

    dob : date
        the date of birth of the student

    degree_choice : str
        the degree choice of the student

    transcripts : binary
        the transcript of the student

    Methods
    -------
    accept_student
        Adds student to the login database, assosiates them with the student group and loads relavent information to the marks database

    reject_student
        Removes the student from the potential student database
    """

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
        """Adds student to the login database, assosiates them with the student group and loads relavent information to the marks database
        """
        # Adds the student to the login table
        x = self.env['res.users'].create(
            {'name': self.first_name, 'email': self.email_address, 'login': self.email_address, 'new_password': self.password})
        # Used to capture the userid before assosiating the student with another group and changing the value of x
        y = x
        # Placing the student in a group
        x.groups_id = self.env['res.groups'].search(
            [("name", "=", "Student")])
        self.env['students'].create({'profile_picture': self.profile_picture, 'first_name': self.first_name, 'last_name': self.last_name,
                                     'email_address': self.email_address, 'id_number': self.id_number, 'dob': self.dob, 'degree_choice': self.degree_choice.degree_name, 'userid': y.id})
        # Used to place all module details, as they were seperated in the degree class relation
        modules = [self.degree_choice.module_1.module_name, self.degree_choice.module_2.module_name, self.degree_choice.module_3.module_name, self.degree_choice.module_4.module_name, self.degree_choice.module_5.module_name, self.degree_choice.module_6.module_name,
                   self.degree_choice.module_7.module_name, self.degree_choice.module_8.module_name, self.degree_choice.module_9.module_name, self.degree_choice.module_10.module_name, self.degree_choice.module_11.module_name, self.degree_choice.module_12.module_name]
        departments = [self.degree_choice.module_1.lecturer.department.department_name, self.degree_choice.module_2.lecturer.department.department_name, self.degree_choice.module_3.lecturer.department.department_name, self.degree_choice.module_4.lecturer.department.department_name, self.degree_choice.module_5.lecturer.department.department_name, self.degree_choice.module_6.lecturer.department.department_name,
                       self.degree_choice.module_7.lecturer.department.department_name, self.degree_choice.module_8.lecturer.department.department_name, self.degree_choice.module_9.lecturer.department.department_name, self.degree_choice.module_10.lecturer.department.department_name, self.degree_choice.module_11.lecturer.department.department_name, self.degree_choice.module_12.lecturer.department.department_name]

        for x in range(12):
            # Adds each module to the marks database
            student_module = modules[x]
            # Adds each deparment to the marks database
            department = departments[x]
            self.env['marks'].create({'userid': y.id, 'student_id_number': self.id_number, 'student_email': self.email_address, 'student_first_name': self.first_name,
                                      'student_last_name': self.last_name, 'department': department, 'module': student_module, 'result': 0})
        # Removes the students from the potential student table after they have been added to the students table
        self.env['student.application'].search(
            [('email_address', '=', self.email_address)]).unlink()

    @api.one
    def reject_student(self):
        """Removes the student from the potential student database
        """
        self.env['student.application'].search(
            [('email_address', '=', self.email_address)]).unlink()
