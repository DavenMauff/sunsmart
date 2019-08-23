from odoo import models, fields, api


class Bookings(models.Model):
    _name = "bookings"
    _description = "Bookings"

    name = fields.Char(string="Name", required=True)
    phone_number = fields.Char(string="Phone Number", required=True)
    email_address = fields.Char(string="Email Address", required=True)
    # This field has to be a string for the HTML form
    seating = fields.Selection(
        selection=[("6", "6"), ("4", "4"), ("2", "2")], required=True)
    table_6 = fields.Char(string="6 Seater", default="No")
    table_4 = fields.Char(string="4 Seater", default="No")
    table_2 = fields.Char(string="2 Seater", default="No")
    con_status = fields.Boolean(string="Confirmation", default=False)

    @api.multi
    def confirm(self):
        for rec in self:
            capicty = []
            capicty.append(self.env['bookings'].search_count(
                ['&', ('seating', '=', "6"), ('con_status', '=', True)]) * 6)
            capicty.append(self.env['bookings'].search_count(
                ['&', ('seating', '=', "4"), ('con_status', '=', True)]) * 4)
            capicty.append(self.env['bookings'].search_count(
                ['&', ('seating', '=', "2"), ('con_status', '=', True)]) * 2)
            capicty_available = 30-sum(capicty)
            print(capicty_available)
            print(self.env['bookings'].search_count([('seating', '=', "6")]))
            left_to_fulfil = 0
            left_to_fulfil = int(self.seating)
            while (left_to_fulfil > 0) and (left_to_fulfil <= capicty_available):
                print("---------------------------------\nLTF:\t", left_to_fulfil)
                if (left_to_fulfil >= 6) and (self.env['bookings'].search_count([('seating', '=', "6")]) <= 1):
                    left_to_fulfil -= 6
                    rec.write({'table_6': "True"})
                    print(left_to_fulfil)
                elif (left_to_fulfil >= 4) and (self.env['bookings'].search_count([('seating', '=', "4")]) <= 2):
                    left_to_fulfil -= 4
                    rec.write({'table_4': "True"})
                    print(left_to_fulfil)
                elif (left_to_fulfil >= 1) and (self.env['bookings'].search_count(
                        [('seating', '=', "2")]) < 8):
                    left_to_fulfil -= 2
                    rec.write({'table_2': "True"})
                    print(left_to_fulfil)

            if (left_to_fulfil <= 0):
                rec.write({'con_status': "True"})

    @api.multi
    def done(self):
        self.env['bookings'].search([
            ('email_address', '=', self.email_address)]).unlink()
