# -*- coding: utf-8 -*-
# from odoo import http


# class Cook(http.Controller):
#     @http.route('/cook/cook/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cook/cook/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cook.listing', {
#             'root': '/cook/cook',
#             'objects': http.request.env['cook.cook'].search([]),
#         })

#     @http.route('/cook/cook/objects/<model("cook.cook"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cook.object', {
#             'object': obj
#         })
