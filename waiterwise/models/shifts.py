from odoo import models, fields, api
from datetime import datetime


class Shifts(models.Model):
    _name = "shifts"
    _description = "Shifts"
    _rec_name = "waiter"

    week_number = fields.Integer(
        string="Week Number", compute='_get_week_number')
    waiter = fields.Many2one("waiters", string="Waiter", required=True, )
    day = fields.Selection(selection=[("monday", "Monday"), ("tuesday", "Tuesday"), ("wednesday", "Wednesday"), (
        "thursday", "Thursday"), ("friday", "Friday"), ("saturday", "Saturday")], string="Weekday", required=True, )
    period = fields.Selection(selection=[(
        "day", "Day"), ("evening", "Evening")], string="Period", required=True, )

    @api.multi
    def _get_week_number(self):
        for record in self:
            record.week_number = datetime.today().isocalendar()[1]
