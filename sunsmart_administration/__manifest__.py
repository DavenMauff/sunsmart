# -*- coding: utf-8 -*-
{
    'name': "SUNSmart",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', ],

    # always loaded
    'data': [
        'security/sunsmart_security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/menu_views.xml',
        'views/marks_view.xml',
        'views/students_view.xml',
        'views/module_view.xml',
        'views/degree_view.xml',
        'views/departments_view.xml',
        'views/lecturer_view.xml',
        'views/user_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
