from odoo import models, fields, api
from odoo.exceptions import ValidationError

class advancedTeam_model(models.Model):
    _inherit = 'tournament_app.team_model'

    minimRank_id = fields.Many2one("touradv_ranks.rank_model",string='Minim rank',help="Minim rank of the players")
    modifer_id = fields.Many2one("res.users",string="Responsible")



