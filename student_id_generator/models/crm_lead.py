from odoo import models, fields, api

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    x_student_id = fields.Char(string="Student ID", related="partner_id.x_student_id", store=True, readonly=True)

    @api.model
    def create(self, vals):
        # Auto-link to partner if email matches and partner_id is not set
        if vals.get('email_from') and not vals.get('partner_id'):
            partner = self.env['res.partner'].search([('email', '=', vals['email_from'])], limit=1)
            if partner:
                vals['partner_id'] = partner.id
            else:
                # If no partner exists with the email, create a new partner
                partner = self.env['res.partner'].create({
                    'name': vals.get('contact_name', ''),
                    'email': vals.get('email_from', ''),
                    # Add other necessary fields for the partner as needed
                })
                vals['partner_id'] = partner.id
        
        # Auto-link to partner if customer_name exists and partner_id is not set
        if vals.get('contact_name') and not vals.get('partner_id'):
            partner = self.env['res.partner'].search([('name', '=', vals['contact_name'])], limit=1)
            if partner:
                vals['partner_id'] = partner.id
            else:
                # If no partner exists with the name, create a new partner
                partner = self.env['res.partner'].create({
                    'name': vals.get('contact_name'),
                    'email': vals.get('email_from', ''),  # Email will be set if available
                    # Add other necessary fields for the partner as needed
                })
                vals['partner_id'] = partner.id

        return super(CrmLead, self).create(vals)
