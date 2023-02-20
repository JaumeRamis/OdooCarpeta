# -*- coding: utf-8 -*-
from datetime import timedelta

from odoo import models, fields

class Paciente(models.Model):
    _name = 'paciente'
    name = fields.Char(string='Nombre', required=True)
    last_name = fields.Char(string='Apellido', required=True)
    symptoms = fields.Char('Sintomas', required=True)
