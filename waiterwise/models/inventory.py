from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Wines(models.Model):
    """
    A class used to represent wine inventory

    ...

    Attributes
    ----------
    name : str
        the name of the wine

    vintage : str
        the vintage of the wine

    varietal : str
        the varietal of the wine

    stock : str
        the current stock count of the wine in inventory

    Methods
    -------
    wine_stock(self)
        Function to automatically place wine inventory items into a 'Orders' table for ease of use. A threshold is defined, and once the stock item has 
        gone below that threshold, it will automatically be moved. The method also holds functionality to to update current stock levels in both the 
        'Orders' and 'Pending Orders' table after the items have been moved, and handle duplications if the item has moved below the threshold again
        from another stock update
    """
    _name = "wines"
    _description = "Wines"

    name = fields.Char(string="Name")
    vintage = fields.Char(string="Vintage")
    varietal = fields.Char(string="Varietal")
    stock = fields.Integer(string="Stock", readonly=False, )

    # As soon as the stock variable in inventory changes, system whether to automatically place the item in an 'Order' table
    @api.onchange('stock')
    def wine_stock(self):
        """Function to automatically place wine inventory items into a 'Orders' table for ease of use. A threshold is defined, and once the stock item has 
        gone below that threshold, it will automatically be moved. The method also holds functionality to to update current stock levels in both the 
        'Orders' and 'Pending Orders' table after the items have been moved, and handle duplications if the item has moved below the threshold again
        from another stock update

        Parameters
        ----------
        self : str
            The items inventory details are passed through the function to update varies other tables
        """
        rec = []

        for record in self:
            # Checks to see if item is already in the 'Orders' table
            # This may occur, if the item passes below the threshold the first time (<5) and then the stock moves downward again from 4 to 3
            # The system in the duplication case will not add a duplicated record but instead update the stock remaining field in the 'Orders" table
            rec = self.env['orders'].search(
                [('name', '=', record.name)])
            if rec:
                # Changes the remaining stock in 'Orders' table if the item is already in the orders table
                rec.write({'remaining_stock': self.stock})
            else:
                # If the item has passed below the threshold and it's not in the 'Orders' table, the item will then be added
                if self.stock < 5:
                    self.env['orders'].create(
                        {'name': self.name, 'vintage': self.vintage, 'varietal': self.varietal, 'expiration_date': '', 'order_type': 'Wine', 'remaining_stock': self.stock, 'order_amount': 0})

        for record in self:
            # If the item is already been moved to the 'Pending Orders' table (i.e. the admin as clicked the Order Button from the 'Orders' table)
            # It will update the stock remaining in that table too
            # This is important, because when the user clicks that they've recieved the order, it will plus on to the existing stock in the inventory tables
            rec = self.env['pending.orders'].search(
                [('name', '=', record.name)])
            if rec:
                # Updates remaining stock if the record appears in the 'Pending Orders' table
                rec.write({'remaining_stock': self.stock})


class Food(models.Model):
    """
    A class used to represent wine inventory

    ...

    Attributes
    ----------
    name : str
        the name of the food item

    expiration_date : str
        the expiration date of the food

    stock : str
        the current stock count of the food 

    Methods
    -------
    food_stock(self)
        Function to automatically place food inventory items into a 'Orders' table for ease of use. A threshold is defined, and once the stock item has 
        gone below that threshold, it will automatically be moved. The method also holds functionality to to update current stock levels in both the 
        'Orders' and 'Pending Orders' table after the items have been moved, and handle duplications if the item has moved below the threshold again
        from another stock update
    """
    _name = "food"
    _description = "Food"

    name = fields.Char(string="Name")
    expiration_date = fields.Char(string="Expiration Date")
    stock = fields.Integer(string="Stock")

    @api.onchange('stock')
    def food_stock(self):
        """Function to automatically place wine inventory items into a 'Orders' table for ease of use. A threshold is defined, and once the stock item has 
        gone below that threshold, it will automatically be moved. The method also holds functionality to to update current stock levels in both the 
        'Orders' and 'Pending Orders' table after the items have been moved, and handle duplications if the item has moved below the threshold again
        from another stock update

        Parameters
        ----------
        self : str
            The items inventory details are passed through the function to update varies other tables
        """

        # Checks to see if item is already in the 'Orders' table
        # This may occur, if the item passes below the threshold the first time (<5) and then the stock moves downward again from 4 to 3
        # The system in the duplication case will not add a duplicated record but instead update the stock remaining field in the 'Orders" table
        for record in self:
            rec = self.env['orders'].search(
                [('name', '=', record.name)])
            if rec:
                # Changes the remaining stock in 'Orders' table if the item is already in the orders table
                rec.write({'remaining_stock': self.stock})
            else:
                # If the item has passed below the threshold and it's not in the 'Orders' table, the item will then be added
                if self.stock < 5:
                    self.env['orders'].create(
                        {'name': self.name, 'vintage': '', 'varietal': '', 'expiration_date': self.expiration_date, 'order_type': 'Food', 'remaining_stock': self.stock, 'order_amount': 0})

        for record in self:
            # If the item is already been moved to the 'Pending Orders' table (i.e. the admin as clicked the Order Button from the 'Orders' table)
            # It will update the stock remaining in that table too
            # This is important, because when the user clicks that they've recieved the order, it will plus on to the existing stock in the inventory tables
            rec = self.env['pending.orders'].search(
                [('name', '=', record.name)])
            if rec:
                # Updates remaining stock if the record appears in the 'Pending Orders' table
                rec.write({'remaining_stock': self.stock})


class Orders(models.Model):
    """
    A class used to represent wine inventory

    ...

    Attributes
    ----------
    name : str
        the name of the order

    vintage : str
        the vintage of the order (wine)

    varietal : str
        the varietal of the order (wine)

    expiration_date : str
        the expiration date of the order (food)

    order_type : str
        the type of order (wine or food)

    remaining_stock : str
        the current stock count of the order in inventory

    order_amount : str
        the amount to be ordered

    Methods
    -------
    submit_order(self)
        Function to submit order, moving the item from the 'Orders' table to the 'Pending Orders' tables. The method will validate only when an order amount
        has been specified and will throw an error otherwise
    """
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

    # Button used to submit the order from the 'Orders' table, moving the order from the 'Orders' table to the 'Pending Orders' table
    @api.one
    """Function to submit order, moving the item from the 'Orders' table to the 'Pending Orders' tables. The method will validate only when an order amount
        has been specified and will throw an error otherwise

        Parameters
        ----------
        self : str
            Information pertaining to the 'Orders' table to submit information when moving the item to the 'Pending Orders' table 
        """

    def submit_order(self):
        # If the user has not entered an order amount, an error will be displayed
        if self.order_amount <= 0:
            raise ValidationError("Please enter an order amount!")
        else:
            # If an order amount has been specified, the order will be moved to the 'Pending Orders' table
            self.env['pending.orders'].create({'name': self.name, 'vintage': self.vintage, 'varietal': self.varietal, 'expiration_date': self.expiration_date,
                                               'order_type': self.order_type, 'remaining_stock': self.remaining_stock, 'order_amount': self.order_amount})
            # Once the order has been submitted, it will be removed from the 'Orders' table becuase it will have been placed in the 'Pending Orders' table
            self.env['orders'].search(
                [('name', '=', self.name)]).unlink()


class PendingOrders(models.Model):
    """
    A class used to represent wine inventory

    ...

    Attributes
    ----------
    name : str
        the name of the order

    vintage : str
        the vintage of the order (wine)

    varietal : str
        the varietal of the order (wine)

    expiration_date : str
        the expiration date of the order (food)

    order_type : str
        the type of order (wine or food)

    remaining_stock : str
        the current stock count of the order in inventory

    order_amount : str
        the amount to be ordered

    Methods
    -------
    recieved_order(self)
        Function to verify an order has been recieved. In doing so, the item will move from the 'Pending Orders' table to the Inventory tables
        The method also contains functionality to check if the item already appears in the inventory table, and therfore will update the stock
        count with the order amount and the current stock amount, if the item does not appear, the function will then create a new item in the 
        table. The function also sifts through the items by type, placing Wine and Food in the 'Wine' and 'Food' table respectively.
    """

    _name = 'pending.orders'
    _description = 'Pending Orders'

    name = fields.Char(string="Name")
    vintage = fields.Char(string="Vintage")
    varietal = fields.Char(string="Varietal")
    expiration_date = fields.Char(string="Expiration Date")
    order_type = fields.Char(string="Type")
    remaining_stock = fields.Integer(string="Remaining Stock")
    order_amount = fields.Integer(string="Order Amount")

    # Button used to specify the order has been recieved, adding it back to the current stock of the item in the inventory tables
    @api.one
    def recieved_order(self):
        """Function to verify an order has been recieved. In doing so, the item will move from the 'Pending Orders' table to the Inventory tables
        The method also contains functionality to check if the item already appears in the inventory table, and therfore will update the stock
        count with the order amount and the current stock amount, if the item does not appear, the function will then create a new item in the 
        table. The function also sifts through the items by type, placing Wine and Food in the 'Wine' and 'Food' table respectively.

        Parameters
        ----------
        self : str
            Information pertaining to the 'Pending Orders' class in order to submit information when transfering the item between tables
        """

        # When totaling variables obtained from the instance of the current class, they're got to be assigned and then assigned variables summed
        current = self.remaining_stock
        recieved = self.order_amount
        # Adding the current stock amount with the recieved stock amount from the order in the 'Pending Orders' table
        # Only one instance of total variables will be needed for both categories wine and food, as logic below handles differentitation
        # See logic explanations below for validity of the above comment
        total = current + recieved
        for record in self:
            # Statement to check what type of item has been recieved so that it can be added to the correct table
            # There is an inventory table for food items and another for wine items
            # Therefore an attribute of 'order_type' is used to differentiate the item recieved
            if self.order_type == 'Wine':
                for record_one in self:
                    # Checks whether the item is already in inventory to update the total
                    # This is important as the user may wish to place an order directly from the 'Orders' that us not part of inventory
                    # This can be replicated by a restaurant adding a new wine to the sales selection
                    rec = self.env['wines'].search(
                        [('name', '=', record_one.name)])
                    if rec:
                        # If the item does already appear, update the stock variable
                        # Note this is the variable that is checked to automatically add the item to the 'Orders' table
                        # Therefore, if this value is below 5, it will be re-added to the 'Orders' table, this is because the threshold is assumed to be five
                        # Thresholds for individual items can be an improvement and a new feature
                        rec.write(
                            {'stock': total})
                    else:
                        # If the item isn't in the inventory tables (different table for wine and food), it will create the item
                        self.env['wines'].create(
                            {'name': self.name, 'vintage': self.vintage, 'varietal': self.varietal, 'stock': self.order_amount})
            else:
                # If this statement is executed, the item is assumed to be of type food, as previous if statement was rejected
                # PLEASE NOTE: no expiration date is assumed from this field, as it is expected the manager to update the expiration date when the item is recieved
                # However, functionality may be added to automatically assume different expiration dates depending on what type of food is recieved
                for record_one in self:
                    # Checks if that item already appears in the 'Food' table
                    rec = self.env['food'].search(
                        [('name', '=', record_one.name)])
                    if rec:
                        # If the item does appear, it will update the stock value of that item
                        rec.write(
                            {'stock': total})
                    else:
                        # If the item does not appear, it will be created
                        self.env['food'].create(
                            {'name': self.name, 'expiration_date': "Please Enter", 'stock': self.order_amount})
