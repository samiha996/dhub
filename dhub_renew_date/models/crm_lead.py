from odoo import models, fields

class CrmLead(models.Model):
    _inherit = 'crm.lead'
    renew_due_date = fields.Date(string='Renew Due Date')
    renewal_followup_done = fields.Boolean(string='Renewal Follow-Up Done', default=False)