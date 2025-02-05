from odoo import models, fields, api

class CrmLead(models.Model):
    _inherit = 'crm.lead'


    agent = fields.Many2one(
        comodel_name='res.partner',string='Agent'
    )

    study_country = fields.Many2one(
        comodel_name='res.country', string='Study Country'
    )



    