from odoo import models, fields, api


class Modules(models.Model):
    """
    A class used to represent a Modules

    ...

    Attributes
    ----------
    module_name : str
        the name of the module

    lecturer : str
        the lecturer who teaches the module
    """

    _name = 'modules'
    _description = 'Modules'
    _rec_name = 'module_name'

    module_name = fields.Char(string="Module Name", required=True, )
    lecturer = fields.Many2one(comodel_name='lecturers',)
