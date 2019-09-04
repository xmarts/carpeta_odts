# -*- coding: utf-8 -*-
from odoo import http

# class Odts(http.Controller):
#     @http.route('/odts/odts/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odts/odts/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odts.listing', {
#             'root': '/odts/odts',
#             'objects': http.request.env['odts.odts'].search([]),
#         })

#     @http.route('/odts/odts/objects/<model("odts.odts"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odts.object', {
#             'object': obj
#         })