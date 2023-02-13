# -*- coding: utf-8 -*-
from datetime import timedelta

from odoo import models, fields

class Socios(models.Model):
    _name = 'socios'
    name = fields.Char(string='Nombre', required=True)
    last_name = fields.Char(string='Apellido', required=True)
    identifier = fields.Integer('Identificador', required=True, index=True)