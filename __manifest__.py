# -*- coding: utf-8 -*-
{
    'name': "Cook",

    'summary': """
        A module to provide information about cooking recipes""",

    'description': """
        This module is created to teach odoo development with a simple example of recipe management
    """,

    'author': "Antoni Oliver Gelabert",
    'website': "https://github.com/tonibois/cook",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Services',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr'],

    # always loaded
    'data': [
        'views/views.xml',
        'views/templates.xml',
        'security/security.xml',
        'security/ir.model.access.csv'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}
