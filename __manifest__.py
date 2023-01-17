# -*- coding: utf-8 -*-
{
    'name': "Test Addons",

    'summary': """
        QUILSOFT exam """,

    'description': """
        QUILSOFT exam """,

    'author': "mjavint@gmail.com",

    'version': '15.0.20230116',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website'],

    # always loaded
    'data': [
        # Views
        'views/res_partner_views.xml',
        'views/res_config_settings_views.xml',
        'views/res_company_views.xml',
        'views/templates.xml',
        'views/snippets.xml',
    ],
}
