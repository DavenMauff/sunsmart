from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Wines(models.Model):
    _name = "wines"
    _description = "Wines"

    name = fields.Char(string="Name")
    vintage = fields.Char(string="Vintage")
    varietal = fields.Char(string="Varietal")
    stock = fields.Integer(string="Stock", readonly=False, )

    @api.onchange('stock')
    def wine_stock(self):
        rec = []

        for record in self:
            rec = self.env['orders'].search(
                [('name', '=', record.name)])
            if rec:
                rec.write({'remaining_stock': self.stock})
            else:
                if self.stock < 5:
                    self.env['orders'].create(
                        {'name': self.name, 'vintage': self.vintage, 'varietal': self.varietal, 'expiration_date': '', 'order_type': 'Wine', 'remaining_stock': self.stock, 'order_amount': 0})

        for record in self:
            rec = self.env['pending.orders'].search(
                [('name', '=', record.name)])
            if rec:
                rec.write({'remaining_stock': self.stock})


class Food(models.Model):
    _name = "food"
    _description = "Food"

    name = fields.Char(string="Name")
    expiration_date = fields.Char(string="Expiration Date")
    stock = fields.Integer(string="Stock")

    @api.onchange('stock')
    def wine_stock(self):

        for record in self:
            rec = self.env['orders'].search(
                [('name', '=', record.name)])
            if rec:
                rec.write({'remaining_stock': self.stock})
            else:
                if self.stock < 5:
                    self.env['orders'].create(
                        {'name': self.name, 'vintage': '', 'varietal': '', 'expiration_date': self.expiration_date, 'order_type': 'Food', 'remaining_stock': self.stock, 'order_amount': 0})

        for record in self:
            rec = self.env['pending.orders'].search(
                [('name', '=', record.name)])
            if rec:
                rec.write({'remaining_stock': self.stock})


class Orders(models.Model):
    _name = "orders"
    _description = "Orders"

    name = fields.Char(string="Name")
    vintage = fields.Char(string="Vintage")
    varietal = fields.Char(string="Varietal")
    expiration_date = fields.Char(string="Expiration Date")
    order_type = fields.Char(string="Type")
    remaining_stock = fields.Integer(string="Remaining Stock")
    # Used 0 here, because even if 0 is passed in from previous classes, if the user creates a new order that is not set from the previous classes of inventory it will populate a default value and therefore is not redundant
    order_amount = fields.Integer(string="Order Amount", default=0, )

    # Add logic to check if the order amount is empty
    @api.one
    def submit_order(self):
        if self.order_amount <= 0:
            raise ValidationError("Please enter an order amount!")
        else:
            self.env['pending.orders'].create({'name': self.name, 'vintage': self.vintage, 'varietal': self.varietal, 'expiration_date': self.expiration_date,
                                               'order_type': self.order_type, 'remaining_stock': self.remaining_stock, 'order_amount': self.order_amount})
            self.env['orders'].search(
                [('name', '=', self.name)]).unlink()


class PendingOrders(models.Model):
    _name = 'pending.orders'
    _description = 'Pending Orders'

    name = fields.Char(string="Name")
    vintage = fields.Char(string="Vintage")
    varietal = fields.Char(string="Varietal")
    expiration_date = fields.Char(string="Expiration Date")
    order_type = fields.Char(string="Type")
    remaining_stock = fields.Integer(string="Remaining Stock")
    order_amount = fields.Integer(string="Order Amount")

    @api.one
    def recieved_order(self):
        current = self.remaining_stock
        recieved = self.order_amount
        total = current + recieved
        print(total)
        for record in self:
            if self.order_type == 'Wine':
                for record_one in self:
                    rec = self.env['wines'].search(
                        [('name', '=', record_one.name)])
                    if rec:
                        rec.write(
                            {'stock': total})
                    else:
                        self.env['wines'].create(
                            {'name': self.name, 'vintage': self.vintage, 'varietal': self.varietal, 'stock': self.order_amount})
            else:
                for record_one in self:
                    rec = self.env['food'].search(
                        [('name', '=', record_one.name)])
                    if rec:
                        rec.write(
                            {'stock': total})
                    else:
                        self.env['food'].create(
                            {'name': self.name, 'expiration_date': "Please Enter", 'stock': self.order_amount})
