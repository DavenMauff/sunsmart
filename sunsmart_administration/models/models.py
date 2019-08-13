
# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Departments(models.Model):
    _name = 'departments'
    _description = 'Departments'
    _rec_name = 'department_name'

    department_name = fields.Char(string="Department Name", required=True, )
    department_name_test = fields.Char(
        string="Department Name Test", required=True, )


class Lecturers(models.Model):
    _name = "lecturers"
    _description = 'Lecturers'

    student_number = student_number = fields.Integer(
        string='SST', default=lambda self: self.env['ir.sequence'].next_by_code('increment_student_number'))
    first_name = fields.Char(string="First Name", required=True, )
    last_name = fields.Char(string="Last Name", required=True, )
    phone_number = fields.Char(string="Phone Number", required=True, )
    id_number = fields.Char(string="ID Number", required=True, )
    department = fields.Many2one(
        comodel_name='departments', )


class Modules(models.Model):
    _name = 'modules'
    _description = 'Modules'

    module_name = fields.Char(string="Module Name", required=True, )
    lecturer = fields.Many2one(
        'lecturers', 'student_number', )


class Degree(models.Model):
    _name = 'degrees'
    _description = 'Degrees'

    degree_name = fields.Char(string="Degree Name", required=True, )
    module_1 = fields.One2many('modules', 'module_name', )
    module_2 = fields.One2many('modules', 'module_name', )
    module_3 = fields.One2many('modules', 'module_name', )
    module_4 = fields.One2many('modules', 'module_name', )
    module_5 = fields.One2many('modules', 'module_name', )
    module_6 = fields.One2many('modules', 'module_name', )
    module_7 = fields.One2many('modules', 'module_name', )
    module_8 = fields.One2many('modules', 'module_name', )
    module_9 = fields.One2many('modules', 'module_name', )
    module_10 = fields.One2many('modules', 'module_name', )
    module_11 = fields.One2many('modules', 'module_name', )
    module_12 = fields.One2many('modules', 'module_name', )
