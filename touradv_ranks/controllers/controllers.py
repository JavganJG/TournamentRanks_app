# -*- coding: utf-8 -*-
# from odoo import http


# class CustomRanksTournamentApp(http.Controller):
#     @http.route('/custom_ranks_tournament_app/custom_ranks_tournament_app/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_ranks_tournament_app/custom_ranks_tournament_app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_ranks_tournament_app.listing', {
#             'root': '/custom_ranks_tournament_app/custom_ranks_tournament_app',
#             'objects': http.request.env['custom_ranks_tournament_app.custom_ranks_tournament_app'].search([]),
#         })

#     @http.route('/custom_ranks_tournament_app/custom_ranks_tournament_app/objects/<model("custom_ranks_tournament_app.custom_ranks_tournament_app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_ranks_tournament_app.object', {
#             'object': obj
#         })
