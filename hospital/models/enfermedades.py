# -*- coding: utf-8 -*-
from datetime import timedelta

from odoo import models, fields

class Enfermedades(models.Model):
    _name = 'enfermedades'
    id = fields.Integer(string='Id', required=True)
    name = fields.Char(string='Nombre', required=True)
    description = fields.Char(string='Descripcion', required=True)