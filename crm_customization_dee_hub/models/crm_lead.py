from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    lead_call_ids = fields.One2many(
        'crm.lead.call',
        'lead_id'
    )
    lead_calls_count = fields.Integer(
        compute='_compute_lead_calls',
        store=True
    )
    substate_id = fields.Many2one(
        comodel_name='crm.substate'
    )

    @api.depends('lead_call_ids')
    def _compute_lead_calls(self):
        for record in self:
            record['lead_calls_count'] = len(record.lead_call_ids)


    


    