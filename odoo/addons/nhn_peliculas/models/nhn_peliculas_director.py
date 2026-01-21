# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date

class nhn_peliculas_director(models.Model):
    _name = 'nhn_peliculas.director'
    _description = 'Director de cine'
    
    name = fields.Char(
        string='Nombre completo',
        required=True,
    )
    
    fecha_nacimiento = fields.Date(
        string='Fecha de nacimiento',
    )
    
    nacionalidad = fields.Char(
        string='Nacionalidad',
    )
    
    biografia = fields.Text(
        string='Biografía',
    )
    
    foto = fields.Image(
        string='Fotografía del director',
    )
    
    # Relación One2many con películas (un director puede dirigir muchas películas)
    pelicula_ids = fields.One2many(
        'nhn_peliculas.pelicula',  # Modelo relacionado
        'director_id',              # Campo en el modelo relacionado
        string='Películas dirigidas'
    )
    
    # Campo calculado para edad
    edad = fields.Integer(
        string='Edad',
        compute='_compute_edad',
        store=False,
    )
    
  