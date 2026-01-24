from odoo import models, fields, api

class Pelicula(models.Model):
    _name = 'nhn_peliculas.pelicula'
    _description = 'Película'
    
    name = fields.Char(string='Título', required=True)
    anio = fields.Integer(string='Año')
    duracion = fields.Integer(string='Duración (minutos)')
    sinopsis = fields.Text(string='Sinopsis')
    imagen = fields.Binary(string='Poster')
    
   
    director_id = fields.Many2one(
        comodel_name='nhn_peliculas.director',
        string='Director',
        required=True
    )
    
    actores_ids = fields.Many2many(
        comodel_name='nhn_peliculas.actor',
        relation='pelicula_actor_rel',
        column1='pelicula_id',
        column2='actor_id',
        string='Actores Principales'
    )
    
    generos_ids = fields.Many2many(
        comodel_name='nhn_peliculas.genero',
        relation='pelicula_genero_rel',
        column1='pelicula_id',
        column2='genero_id',
        string='Géneros'
    )
    
    # Campo calculado
    nombre_completo = fields.Char(
        string='Película Completa',
        compute='_compute_nombre_completo',
        store=True
    )
    
    @api.depends('name', 'anio')
    def _compute_nombre_completo(self):
        for record in self:
            if record.anio:
                record.nombre_completo = f"{record.name} ({record.anio})"
            else:
                record.nombre_completo = record.name