# -*- coding: utf-8 -*-
from datetime import timedelta

from odoo import models, fields

class Modulo(models.Model):
    _name = 'modulo'
    nModulo = fields.Char(string='Nombre del Modulo', required=True)
    nAlumno = fields.Many2many('alumno',string='Alumno', required=True, index=True)
    nProfesor = fields.Many2many('profesor',string='Profesor', required=True, index=True)