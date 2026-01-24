# -*- coding: utf-8 -*-
{
    'name': "Cartelera",

    'summary': "Peliculas disponibles en cartelera",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    #mmmmmm
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/nhn_peliculas_actor.xml',
        'views/nhn_peliculas_director.xml',
        'views/nhn_peliculas_genero.xml',
        'views/nhn_peliculas_pelicula.xml',
        'views/menus.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True
}

