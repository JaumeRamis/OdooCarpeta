# -*- coding: utf-8 -*-
from datetime import timedelta

from odoo import models, fields

class Director(models.Model):
    _name = 'director'
    name = fields.Char(string='Nombre', required=True)
    last_name = fields.Char(string='Apellido', required=True)