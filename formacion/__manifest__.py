# -*- coding: utf-8 -*-
{
    'name': "formacion",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Ciclos Formativos. Ejercicio 5.9
    """,

    'application': True,
    'author': "Jaume Goñalons",
    'website': "http://iesjoanramis.org",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/ciclo_view.xml',
        'views/alumno_view.xml',
        'views/modulo_view.xml',
        'views/profesor_view.xml',
    ],
    # only loaded in demonstration mode
    #'demo': [
    #    'demo/demo.xml',
    #],
}
