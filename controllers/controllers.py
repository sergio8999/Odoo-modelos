# -*- coding: utf-8 -*-
# from odoo import http


# class Odoo644(http.Controller):
#     @http.route('/odoo644/odoo644/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo644/odoo644/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo644.listing', {
#             'root': '/odoo644/odoo644',
#             'objects': http.request.env['odoo644.odoo644'].search([]),
#         })

#     @http.route('/odoo644/odoo644/objects/<model("odoo644.odoo644"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo644.object', {
#             'object': obj
#         })
