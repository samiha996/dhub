from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo import http
from odoo.http import request


class CustomWebsiteSale(WebsiteSale):
    def checkout_check_address(self, order):
        """ Override this method to skip address validation completely. """
        return  # Do nothing, preventing redirection to /shop/address

    @http.route(['/shop/checkout'], type='http', auth="public", website=True, sitemap=False)
    def checkout(self, **post):
        """
        Custom checkout: Skip billing/shipping steps and go directly to payment.
        """
        order = request.website.sale_get_order()

        # Ensure the order exists
        if not order or order.state != 'draft':
            return request.redirect('/shop')

        # Assign the same partner to shipping & invoice to bypass address validation
        order.partner_shipping_id = order.partner_id
        order.partner_invoice_id = order.partner_id

        # Ensure address validation does not happen
        return request.redirect('/shop/payment')

    @http.route(['/shop/payment'], type='http', auth="public", website=True, sitemap=False)
    def shop_payment(self, **post):
        """
        Ensure checkout always skips addresses and lands directly on payment.
        """
        order = request.website.sale_get_order()

        if not order or order.state != 'draft':
            return request.redirect('/shop')

        # Ensure the order is ready for payment
        return super().shop_payment(**post)
