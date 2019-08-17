from odoo import models, fields, api


class Marks(models.Model):
    """
    A class used to represent students Marks

    ...

    Attributes
    ----------
    userid : binary
        the unique user id assosiated with the student login database

    student_id_number : str
        the students id number

    student_email : str
        the students email address

    student_first_name : str
        the students first name

    student_last_name : str
        the students last name

    department : str
        the department of the module for the row asosiated with the student

    module : str
        the module of the row assosiated with the student

    result : int
        the result per module for the student

    Methods
    -------
    onchange_result(result)
        Used to check the mark was assosaited with the correct student

    """

    _name = "marks"
    _description = "Marks"

    userid = fields.Char(string="userid")
    student_id_number = fields.Char(string="ID Number")
    student_email = fields.Char(string="Email")
    student_first_name = fields.Char(string="First Name")
    student_last_name = fields.Char(string="Last Name")
    department = fields.Char(string="Department")
    module = fields.Char(string="Module")
    result = fields.Integer(string="Result")

    @api.onchange('result')
    def onchange_result(self):
        """Used to check the mark was assosaited with the correct student

        Parameters
        ----------
        id_number : int
            the result per module for the student
        """
        print(self.result)
        print(self.student_id_number)
