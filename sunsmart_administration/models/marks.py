from odoo import models, fields, api


class Marks(models.Model):
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

    # @api.multi
    # def mark_filter(self):
    #     desired_group_name = self.env['res.groups'].search(
    #         [('name', '=', 'Lecturer')])
    #     is_desired_group = self.env.user.id in desired_group_name.users.ids
    #     print(is_desired_group)

    @api.onchange('result')
    def onchange_result(self):
        print(self.result)
        print(self.student_id_number)


# @api.model:
# def create(self, values):
#     print("--------------------------------------------it worked----------------------------------------------")
#     autoRun()
#     return super(test, self).create(values)
