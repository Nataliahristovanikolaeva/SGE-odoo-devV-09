from odoo import models, fields, api

class Director(models.Model):
    _name = 'nhn_peliculas.director'
    _description = 'Director'
    
    name = fields.Char(string='Nombre', required=True)
    fecha_nacimiento = fields.Date(string='Fecha de Nacimiento')
    nacionalidad = fields.Char(string='Nacionalidad')
    premios = fields.Text(string='Premios y Reconocimientos')
    
    
    peliculas_ids = fields.One2many(
        comodel_name='nhn_peliculas.pelicula',
        inverse_name='director_id',  
        string='Películas'
    )