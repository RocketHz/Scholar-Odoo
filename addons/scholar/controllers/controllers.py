# -*- coding: utf-8 -*-
# from odoo import http


# class Scholar(http.Controller):
#     @http.route('/scholar/scholar', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/scholar/scholar/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('scholar.listing', {
#             'root': '/scholar/scholar',
#             'objects': http.request.env['scholar.scholar'].search([]),
#         })

#     @http.route('/scholar/scholar/objects/<model("scholar.scholar"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('scholar.object', {
#             'object': obj
#         })

