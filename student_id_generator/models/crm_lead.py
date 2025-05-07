from odoo import models, fields, api

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    x_student_id = fields.Char(string="Student ID", related="partner_id.x_student_id", store=True, readonly=True)

    @api.model
    def create(self, vals):
        # Auto-link to partner if email matches and partner_id not set
        if vals.get('email_from') and not vals.get('partner_id'):
            partner = self.env['res.partner'].search([('email', '=', vals['email_from'])], limit=1)
            if partner:
                vals['partner_id'] = partner.id
        return super(CrmLead, self).create(vals)
