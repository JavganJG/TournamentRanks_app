# -*- coding: utf-8 -*-

from xml.etree.ElementTree import TreeBuilder
from odoo import models, fields, api


class RankModel(models.Model):
    _name = 'touradv_ranks.rank_model'
    _description = 'touradv_ranks.rank_model'

    name = fields.Char(string="name",help="Rank name",required=True,index=True)
    game_id = fields.Many2one("tournament_app.game_model",string='Game',help="Team",required=True)
    leveled = fields.Integer(string="Leveled",required=True)
    image = fields.Binary(string="Image")
 

