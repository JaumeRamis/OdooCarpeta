# -*- coding: utf-8 -*-
from datetime import timedelta

from odoo import models, fields

class Medico(models.Model):
    _name = 'medico'
    name = fields.Char(string='Nombre', required=True)
    last_name = fields.Char(string='Apellido', required=True)
    number = fields.Integer(string='Numero de Colegiado', required=True)