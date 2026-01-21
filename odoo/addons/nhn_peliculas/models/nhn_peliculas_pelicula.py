# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date

class nhn_peliculas_pelicula(models.Model):
    _name = 'nhn_peliculas.pelicula'
    _description = 'Película'
   

    name = fields.Char(
        string='Título',
       
    )
    
    
    fecha_estreno = fields.Date(
        string='Fecha de estreno',
       
    )
    
    duracion = fields.Integer(
        string='Duración (minutos)',
       
    )
    
    sinopsis = fields.Text(
        string='Sinopsis',
     
    )
    
    
    valoracion = fields.Selection([
        ('1', '⭐ - Muy mala'),
        ('2', '⭐⭐ - Mala'),
        ('3', '⭐⭐⭐ - Regular'),
        ('4', '⭐⭐⭐⭐ - Buena'),
        ('5', '⭐⭐⭐⭐⭐ - Excelente'),
    ], 
    string='Valoración',
    default='3',
  
    )
    
    imagen=fields.Image('Imagen de la película')
    
  
    
 