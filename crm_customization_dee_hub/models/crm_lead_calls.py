from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class CrmLeadCall(models.Model):
    _name = 'crm.lead.call'

    summary = fields.Text()
    note = fields.Html()
    lead_id = fields.Many2one(comodel_name='crm.lead', required=True)
    date_deadline = fields.Date()
    user_id = fields.Many2one(comodel_name='res.users')


    
