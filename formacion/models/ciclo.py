# -*- coding: utf-8 -*-
from datetime import timedelta

from odoo import models, fields

class Ciclo(models.Model):
    _name = 'ciclo'
    nCiclo = fields.Char(string='Nombre del Ciclo', required=True)
    modulos = fields.Many2many('modulo', string='Modulos')