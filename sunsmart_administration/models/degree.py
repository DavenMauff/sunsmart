from odoo import models, fields, api


class Degree(models.Model):
    """
    A class used to represent a Degree

    ...

    Attributes
    ----------
    name : str
        a string used in transfering degree name between seperate modules

    degree_name : str
        the name of a degree

    module_1 : str
        the name of the first module relation within a degree

    module_2 : str
        the name of the second module relation within a degree

    module_3 : str
        the name of the third module relation within a degree

    module_4 : str
        the name of the fourth module relation within a degree

    module_5 : str
        the name of the fifth module relation within a degree

    module_6 : str
        the name of the sixth module relation within a degree

    module_7 : str
        the name of the seventh module relation within a degree

    module_8 : str
        the name of the eigth module relation within a degree

    module_9 : str
        the name of the ninth module relation within a degree

    module_10 : str
        the name of the tenth module relation within a degree

    module_11 : str
        the name of the eleventh module relation within a degree

    module_12 : str
        the name of the twelvth module relation within a degree

    Methods
    -------
    _get_degree_name(self)
        Assigns the degree_name to the name attribute to transpose the correct variable name between models, and especially within the form view, where the call function is primarly on the name attribute
    """

    _name = 'degrees'
    _description = 'Degrees'
    _rec_name = 'degree_name'

    name = fields.Char(compute="_get_degree_name", default="Create Degree")
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

    @api.multi
    def _get_degree_name(self):
        for record in self:
            record.name = record.degree_name
