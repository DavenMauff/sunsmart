# -*- coding: utf-8 -*-
{
    'name': "waiterwise",

    'summary': """
        Waiterwise is the all-in-one restuarant solution!""",

    'description': """
        Solves problems relating to orders, shifting, waiter application and online booking!
    """,

    'author': "Waiterwise",
    'website': "http://www.waiterwise.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/waiterwise_security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/waiters_view.xml',
        'views/menu_view.xml',
        'views/shifts_view.xml',
        'views/inventory_view.xml',
        'views/orders_view.xml',
        'views/bookings_view.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
