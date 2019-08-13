
# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Departments(models.Model):  # done
    _name = 'departments'
    _description = 'Departments'
    _rec_name = 'department_name'

    department_name = fields.Char(string="Department Name", required=True, )
    department_name_test = fields.Char(
        string="Department Name Test", required=True, )


class Lecturers(models.Model):  # done
    _name = "lecturers"
    _description = 'Lecturers'
    _rec_name = 'student_number'  # this is the unique identifier but do we want name?

    student_number = student_number = fields.Integer(
        string='SST', default=lambda self: self.env['ir.sequence'].next_by_code('increment_student_number'))
    first_name = fields.Char(string="First Name", required=True, )
    last_name = fields.Char(string="Last Name", required=True, )
    phone_number = fields.Char(string="Phone Number", required=True, )
    id_number = fields.Char(string="ID Number", required=True, )
    department = fields.Many2one(
        comodel_name='departments', )


class Modules(models.Model):  # done
    _name = 'modules'
    _description = 'Modules'
    _rec_name = 'module_name'

    module_name = fields.Char(string="Module Name", required=True, )
    lecturer = fields.Many2one(comodel_name='lecturers',)


class Degree(models.Model):
    _name = 'degrees'
    _description = 'Degrees'

    degree_name = fields.Char(string="Degree Name", required=True, )
    module_1 = fields.Many2one(comodel_name='modules', )
    module_2 = fields.Many2one(comodel_name='modules', )
    module_3 = fields.Many2one(comodel_name='modules', )
    module_4 = fields.Many2one(comodel_name='modules', )
    module_5 = fields.Many2one(comodel_name='modules', )
    module_6 = fields.Many2one(comodel_name='modules', )
    module_7 = fields.Many2one(comodel_name='modules', )
    module_8 = fields.Many2one(comodel_name='modules', )
    module_9 = fields.Many2one(comodel_name='modules', )
    module_10 = fields.Many2one(comodel_name='modules', )
    module_11 = fields.Many2one(comodel_name='modules', )
    module_12 = fields.Many2one(comodel_name='modules', )
