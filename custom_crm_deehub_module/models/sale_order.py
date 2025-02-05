from odoo import models, fields,api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    substate_id = fields.Many2one(
        comodel_name='crm.substate',related='opportunity_id.substate_id'
    )
    agent = fields.Many2one(
        comodel_name='res.partner', related='opportunity_id.agent'
    )

    lead_calls_count = fields.Integer(
        related='opportunity_id.lead_calls_count'
    )
    study_country = fields.Many2one(
        comodel_name='res.country',related='opportunity_id.study_country', string='Study Country'
    )



