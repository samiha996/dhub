from odoo import models, fields,api

class ProductAttributeValue(models.Model):
    _inherit = 'product.attribute.value'

    calendar_date = fields.Date(string="Calendar", help="Date for Calendar Display Type")
    