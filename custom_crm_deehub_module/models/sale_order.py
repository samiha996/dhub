from odoo import models, fields,api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    substate_id = fields.Many2one(
        comodel_name='crm.substate',related='opportunity_id.substate_id'
    )
    agent = fields.Many2one(
        comodel_name='res.partner', related='opportunity_id.agent'
    )

    related_lead_call_ids = fields.One2many(
        comodel_name="crm.lead.call",
        inverse_name="lead_id",
        string="Related Lead Calls",
        compute="_compute_related_lead_calls",
        store=True
    )

    lead_calls_count = fields.Integer(
        related='opportunity_id.lead_calls_count'
    )
    study_country = fields.Many2one(
        comodel_name='res.country',related='opportunity_id.study_country', string='Study Country'
    )

    @api.depends("opportunity_id")
    def _compute_related_lead_calls(self):
        for record in self:
            if record.opportunity_id:
                record.related_lead_call_ids = record.opportunity_id.lead_call_ids
            else:
                record.related_lead_call_ids = False

