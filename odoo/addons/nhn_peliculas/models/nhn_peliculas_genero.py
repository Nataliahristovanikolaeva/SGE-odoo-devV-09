# -*- coding: utf-8 -*-

from odoo import models, fields

class nhn_peliculas_genero(models.Model):
    _name = 'nhn_peliculas.genero'
    _description = 'Género cinematográfico'
    
    name = fields.Char(
        string='Nombre del género',
        required=True,
    )
    
    descripcion = fields.Text(
        string='Descripción',
    )
    
    # Relación One2many con películas (un género puede tener muchas películas)
    pelicula_ids = fields.One2many(
        'nhn_peliculas.pelicula',  # Modelo relacionado
        'genero_id',               # Campo en el modelo relacionado
        string='Películas de este género'
    )