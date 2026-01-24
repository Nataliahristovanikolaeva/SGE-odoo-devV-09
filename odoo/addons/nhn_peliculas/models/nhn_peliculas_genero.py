from odoo import models, fields, api

class Genero(models.Model):
    _name = 'nhn_peliculas.genero'
    _description = 'Género Cinematográfico'
    
    name = fields.Char(string='Nombre', required=True)
    descripcion = fields.Text(string='Descripción')
    
    peliculas_ids = fields.Many2many(
        'nhn_peliculas.pelicula',
        string='Películas'
    )