# -*- coding: utf-8 -*-
{
    'name': "MyModule",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        very first odoo module
    """,

    'author': "Kairzhanov Murat Kairatovich",
    'website': "http://www.yourcompany.com",


    'category': 'Uncategorized',
    'version': '0.1',


    'depends': ['base',],


    'data': [
        'security/ir.model.access.csv',
        'views/students.xml',
        'views/templates.xml',
        'views/subjects.xml',
        'views/schools.xml',
        'views/teachers.xml',
    ],

    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'auto_install': False,
    'licence': 'LGPL-3'
}
