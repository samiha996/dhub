from odoo import models, fields

class ProductAttribute(models.Model):
    _inherit = 'product.attribute'


    display_type = fields.Selection(
        selection_add=[('calendar', 'Calendar')],
        ondelete={'calendar': 'cascade'},
    )
