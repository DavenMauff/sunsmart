# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Lecturers(models.Model):
    _name = 'dirtygrandpa.lecturers'
    _description = 'Dirty Grandpa Lecturers'

    name = fields.Char(string="Title", required=True)
    description = fields.Text()
