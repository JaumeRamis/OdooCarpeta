# -*- coding: utf-8 -*-
from datetime import timedelta

from odoo import models, fields

class Diagnostico(models.Model):
    _name = 'diagnostico'
    nPaciente = fields.Many2one('paciente',string='Paciente', required=True, index=True)
    nMedico = fields.Many2one('medico',string='Medico', required=True, index=True)
    description = fields.Many2many('enfermedades', string='Diagnostico')