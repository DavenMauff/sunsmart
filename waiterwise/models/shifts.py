from odoo import models, fields, api
from datetime import datetime


class Shifts(models.Model):
    _name = "shifts"
    _description = "Shifts"
    _rec_name = "waiter"

    # Week number will be automatically created each time a shift is done
    # This is to differentiate between weeks in the year and has three advantages:
    # 1. It allows the admin to input shifts for more than one week at a time and won't have to delete records to keep adding per week
    # 2. Once a waiter is logged in, they are able to see exactly which week there shift corresponds to
    # 3. Lastly, a week attribute will allow for efficient filtering when doing so by current week, therefore waiters won't need to scroll through lots of previous records to see current shifts
    week_number = fields.Integer(
        string="Week Number", compute='_get_week_number')
    waiter = fields.Many2one("waiters", string="Waiter", required=True, )
    day = fields.Selection(selection=[("monday", "Monday"), ("tuesday", "Tuesday"), ("wednesday", "Wednesday"), (
        "thursday", "Thursday"), ("friday", "Friday"), ("saturday", "Saturday")], string="Weekday", required=True, )
    period = fields.Selection(selection=[(
        "day", "Day"), ("evening", "Evening")], string="Period", required=True, )

    # Runs to compute the week-number every time the table is requested
    @api.multi
    def _get_week_number(self):
        for record in self:
            # Returns the current week number and assigns it to the weeknumber record in the table
            record.week_number = datetime.today().isocalendar()[1]
