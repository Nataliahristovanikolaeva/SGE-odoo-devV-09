from odoo import models, fields, api

class Actor(models.Model):
    _name = 'nhn_peliculas.actor'
    _description = 'Actor'
    
    name = fields.Char(string='Nombre', required=True)
    fecha_nacimiento = fields.Date(string='Fecha de Nacimiento')
    nacionalidad = fields.Char(string='Nacionalidad')
    biografia = fields.Text(string='Biografía')
    

    peliculas_ids = fields.Many2many(
        'nhn_peliculas.pelicula',
        string='Películas'
    )