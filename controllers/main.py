import json

import werkzeug

from odoo import http
from odoo.http import request, Response


class HomeController(http.Controller):

    @http.route(['/holamundo'], type="http", auth="public",
                method=['GET'],
                csrf=False)
    def hello_world(self, **kw):
        return request.render('test_addons.helloworld', {})

    @http.route(['/hola/<name>'], type="http", auth="public", csrf=False)
    def hello(self, name, **kw):
        return request.render('test_addons.hello_name', {'name': name})

    @http.route(['/products/<model("product.product"):product>'], auth="public", )
    def product1(self, product):
        return request.render('test_addons.product1', {'product': product})

    #  curl --location --request GET 'http://localhost:8069/api/v1/product/5'
    @http.route(['/api/v1/product/<int:product_id>'], type="http",
                auth="public")
    def get_product1(self, product_id):
        product = request.env['product.product'].sudo().search([('id', '=',
                                                                 product_id)])
        vals = {
            'id': product.id,
            'list_price': product.list_price,
            'default_code': product.default_code,
            'standard_price': product.standard_price,
        }
        if request.env.company.api_token != '123456789':
            raise werkzeug.exceptions.BadRequest()
        headers = {
            'Content-Type': 'application/json',
        }
        return Response(json.dumps(vals), status=200, headers=headers)

