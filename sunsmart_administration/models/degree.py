from odoo import models, fields, api


class Degree(models.Model):
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
