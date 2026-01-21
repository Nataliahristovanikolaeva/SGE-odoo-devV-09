# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date

class nhn_peliculas_actor(models.Model):
    _name = 'nhn_peliculas.actor'
    _description = 'Actor/Actriz'
    
    name = fields.Char(
        string='Nombre artístico',
        required=True,
    )
    
    nombre_real = fields.Char(
        string='Nombre real',
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
        string='Fotografía del actor',
    )
    
    # Relación Many2many con películas (un actor puede actuar en muchas películas)
    pelicula_ids = fields.Many2many(
        'nhn_peliculas.pelicula',          # Modelo relacionado
        'pelicula_actor_rel',              # Nombre de la tabla intermedia
        'actor_id',                        # Campo en la tabla intermedia para este modelo
        'pelicula_id',                     # Campo en la tabla intermedia para el modelo relacionado
        string='Películas en las que actúa'
    )
    
    # Campo calculado para edad
    edad = fields.Integer(
        string='Edad',
        compute='_compute_edad',
        store=False,
    )
    
    @api.depends('fecha_nacimiento')
    def _compute_edad(self):
        """Calcula la edad del actor a partir de la fecha de nacimiento"""
        today = date.today()
        for actor in self:
            if actor.fecha_nacimiento:
                edad = today.year - actor.fecha_nacimiento.year
                # Ajustar si aún no ha llegado el cumpleaños este año
                if (today.month, today.day) < (actor.fecha_nacimiento.month, actor.fecha_nacimiento.day):
                    edad -= 1
                actor.edad = edad
            else:
                actor.edad = 0