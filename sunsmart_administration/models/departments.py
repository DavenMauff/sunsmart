from odoo import models, fields, api


class Departments(models.Model):
    _name = 'departments'
    _description = 'Departments'
    _rec_name = 'department_name'

    department_name = fields.Char(string="Department Name", required=True, )
