from odoo import models, fields, api


class Bookings(models.Model):
    """
    A class used to represent bookings made for the resturant

    ...

    Attributes
    ----------
    name : str
        name of the booking

    phone_number : str
        the phone number of the booking

    email_address : str
        the email address of the booking

    seating : str
        the amount of seats required for the booking

    table_6 : str
        representing what tables the booking has (e.g. USE CASE: 1 six seater OR 1 four seater + 1 two seater)

    table_4 : str
        representing what tables the booking has (e.g. USE CASE: 1 six seater OR 1 four seater + 1 two seater)

    table_2 : str
        representing what tables the booking has (e.g. USE CASE: 1 six seater OR 1 four seater + 1 two seater)

    Methods
    -------
    confirm(self)
        Checks the length of a ID number for verification

    done(self)
        Checks the length of a phone number for verification 
    """

    _name = "bookings"
    _description = "Bookings"

    name = fields.Char(string="Name", required=True)
    phone_number = fields.Char(string="Phone Number", required=True)
    email_address = fields.Char(string="Email Address", required=True)
    # This field has to be a string for the HTML form
    # However, can be converted later on to be integrated with the logic
    seating = fields.Selection(
        selection=[("6", "6"), ("4", "4"), ("2", "2")], required=True)
    table_6 = fields.Char(string="6 Seater", default="No")
    table_4 = fields.Char(string="4 Seater", default="No")
    table_2 = fields.Char(string="2 Seater", default="No")
    # Duel purpose with button selection
    con_status = fields.Boolean(string="Confirmation", default=False)

    @api.multi
    def confirm(self):
        for rec in self:
            capicty = []
            # Count is able to dynamically update this way, for example when a table leaves i.e. opening up space for more tables, each time the function runs, it recounts
            # Count's amount of six seaters and multiple to find amount of people
            capicty.append(self.env['bookings'].search_count(
                ['&', ('seating', '=', "6"), ('con_status', '=', True)]) * 6)
            # Count's amount of four seaters and multiple to find amount of people
            capicty.append(self.env['bookings'].search_count(
                ['&', ('seating', '=', "4"), ('con_status', '=', True)]) * 4)
            # Count's amount of two seaters and multiple to find amount of people
            capicty.append(self.env['bookings'].search_count(
                ['&', ('seating', '=', "2"), ('con_status', '=', True)]) * 2)
            # Add all number appended above and minus by the total capicity assumed for the restuarant
            capicty_available = 30-sum(capicty)
            left_to_fulfil = 0
            # Sets variable to the amount of seating requested by the current booking
            left_to_fulfil = int(self.seating)
            # Runs if there are still places to fill from the booking and there IS enough capicity in the resturant between table assignments
            while (left_to_fulfil > 0) and (left_to_fulfil <= capicty_available):
                # If the initial seating is above six and there are six seaters available
                if (left_to_fulfil >= 6) and (self.env['bookings'].search_count([('seating', '=', "6")]) <= 1):
                    left_to_fulfil -= 6
                    # Assigns table a six seater
                    rec.write({'table_6': "True"})
                    # If the booking request is above 4, but assumed lower than six because it passed previous if statement and there is still 4 seaters available
                elif (left_to_fulfil >= 4) and (self.env['bookings'].search_count([('seating', '=', "4")]) <= 2):
                    left_to_fulfil -= 4
                    # Assigns table a four seater
                    rec.write({'table_4': "True"})
                    # If the booking request is larger than one and passed the previous if statment and there are still two seaters available
                    # In this instance, the program will also assign 1 seaters to a table of 2, essentially rounding up as the restuarant doesn't have 1 seaters
                elif (left_to_fulfil >= 1) and (self.env['bookings'].search_count(
                        [('seating', '=', "2")]) < 8):
                    left_to_fulfil -= 2
                    # Assigns the table a 1 seater
                    rec.write({'table_2': "True"})
            # if there are negative or zero places left to fill, change the status to confirmed
            # Variable might become negative because it rounds up 1 seaters to seat them at a table of 2, because there are only 2 seaters
            if (left_to_fulfil <= 0):
                # Change the status
                rec.write({'con_status': "True"})

    @api.multi
    def done(self):
        # Once a table finishes and the admin clicks 'DONE', it will remove the seating from the system to reallocate the space to other potential bookings
        self.env['bookings'].search([
            ('email_address', '=', self.email_address)]).unlink()
