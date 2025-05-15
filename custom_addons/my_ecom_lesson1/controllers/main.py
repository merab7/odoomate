from odoo import http
from odoo.http import request

class MyEcomController(http.Controller):

    @http.route('/products', type='http', auth='public', website=True)
    def my_products(self):
        products = request.env['product.template'].search([('sale_ok', '=', True)], limit=5)
        return request.render('my_ecom_lesson1.product_page', {
            'products': products,
        })
