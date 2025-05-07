from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    x_student_id = fields.Char(string="Student ID", related="partner_id.x_student_id", store=True, readonly=True)
