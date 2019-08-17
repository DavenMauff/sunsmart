from odoo import models, fields, api


class Departments(models.Model):
    """
    A class used to represent a Department

    ...

    Attributes
    ----------
    department_name : str
        The name of a department
    """

    _name = 'departments'
    _description = 'Departments'
    _rec_name = 'department_name'

    department_name = fields.Char(string="Department Name", required=True, )
