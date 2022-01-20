# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class odoo644(models.Model):
#     _name = 'odoo644.odoo644'
#     _description = 'odoo644.odoo644'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100


from odoo import models, fields, api

class pelicula(models.Model):
	_name = 'odoo644.pelicula'
	_description = 'model pelicula'

	name = fields.Integer('id',required=True,unique=True)
	titulo = fields.Char(string='Titulo',required=True)
	director = fields.Char(string='Director', required=True)
	calificacion = fields.Float(string='Calificación',required=True,digits=(6, 2))
	fecha = fields.Date(string='Fecha', required=True)

class director(models.Model):
	_name = 'odoo644.director'
	_description = 'model director'

	name = fields.Integer('id',required=True,unique=True)
	nombre = fields.Char(string='Nombre',required=True)
	pais = fields.Char(string='Pais', required=True)
	pelicula = fields.Char(string='Peicula',required=True)
	fechaNacimiento = fields.Date(string='Fecha nacimiento', required=True)

class actor(models.Model):
	_name = 'odoo644.actor'
	_description = 'model actor'

	name = fields.Integer('id',required=True,unique=True)
	nombre = fields.Char(string='Nombre',required=True)
	pais = fields.Char(string='Pais', required=True)
	pelicula = fields.Char(string='Peicula',required=True)
	fechaNacimiento = fields.Date(string='Fecha nacimiento', required=True)