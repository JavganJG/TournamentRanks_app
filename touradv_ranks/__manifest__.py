# -*- coding: utf-8 -*-
{
    'name': "touradv_ranks",

    'summary': """
        This app is a modify of players of tournament_app""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['tournament_app'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/advancedTeam_view.xml',
        'views/advancedPlayer_view.xml',
        'views/rank_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
}
