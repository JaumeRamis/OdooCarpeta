# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Socios(models.Model):
    _name = 'biblioteca.comic.socios'
    _description = 'Socios'
    name = fields.Char("Nombre")