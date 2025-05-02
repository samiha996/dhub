from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    renew_due_date = fields.Date(string='Renew Due Date')
    renewal_followup_done = fields.Boolean(string='Renewal Follow-Up Done', default=False)