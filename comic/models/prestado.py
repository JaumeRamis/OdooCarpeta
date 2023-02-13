# -*- coding: utf-8 -*-
from datetime import timedelta

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Prestado(models.Model):
    _name = 'prestado'

    ############################################################################################
    nPrestado = fields.Many2one('socios',string='Cliente', required=True, index=True)
    nComic = fields.Many2one('biblioteca.comic',string='Comic prestado', required=True, index=True)
    iniPrestado = fields.Date(string='Fecha de inicio del prestamo')
    finPrestado = fields.Date(string='Fecha de final del prestamo')

    @api.constrains('iniPrestado')
    def _check_initial_date(self):
        for record in self:
            if record.iniPrestado and record.iniPrestado < fields.Date.today():
                raise models.ValidationError('La fecha del prestamo tiene que ser posteriora la actual')

    @api.constrains('finPrestado')
    def _check_final_date(self):
        for record in self:
            if record.finPrestado and record.finPrestado < record.iniPrestado:
                raise models.ValidationError('La fecha de devolución no puede ser anterior a la del prestamo')
