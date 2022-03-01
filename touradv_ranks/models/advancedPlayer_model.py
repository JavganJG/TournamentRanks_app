from odoo import models, fields, api
from odoo.exceptions import ValidationError

class advancedPlayer_model(models.Model):
    _inherit = 'tournament_app.player_model'
    

    #rank_id = fields.Char()
    rank_id = fields.Many2one("touradv_ranks.rank_model",string='Rank',help="Rank of the player")
    last_rank_id = fields.Many2one("touradv_ranks.rank_model",string='Last Rank',help="Last Rank of the player")


