# -*- coding: utf-8 -*-
# from odoo import http


# class DataFactura(http.Controller):
#     @http.route('/data_factura/data_factura', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/data_factura/data_factura/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('data_factura.listing', {
#             'root': '/data_factura/data_factura',
#             'objects': http.request.env['data_factura.data_factura'].search([]),
#         })

#     @http.route('/data_factura/data_factura/objects/<model("data_factura.data_factura"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('data_factura.object', {
#             'object': obj
#         })

