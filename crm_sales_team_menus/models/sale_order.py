from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    team_id = fields.Many2one('crm.team', string='Sales Team')
    
    

    
    