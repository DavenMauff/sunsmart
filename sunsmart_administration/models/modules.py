from odoo import models, fields, api


class Modules(models.Model):
    _name = 'modules'
    _description = 'Modules'
    _rec_name = 'module_name'

    module_name = fields.Char(string="Module Name", required=True, )
    lecturer = fields.Many2one(comodel_name='lecturers',)
