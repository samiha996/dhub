from odoo import models, fields, api,_
from odoo.exceptions import UserError, ValidationError
from markupsafe import Markup
from odoo.tools import html2plaintext


class CrmLeadCall(models.Model):
    _inherit = 'crm.lead.call'


    @api.model
    def create(self, vals):
        record = super(CrmLeadCall, self).create(vals)
        if record.lead_id:
            message = Markup("""
                           <p><b>New Call Logged</b></p>
                           <ul>
                       """)
            if record.summary:
                message += Markup("<li><b>Summary:</b> %s</li>") % record.summary
            if record.date_deadline:
                message += Markup("<li><b>Deadline:</b> %s</li>") % record.date_deadline
            if record.user_id:
                message += Markup("<li><b>Assigned to:</b> %s</li>") % record.user_id.name
            if record.note:
                message += Markup("<li><b>Note:</b> %s</li>") % record.note
            message += Markup("</ul>")

            record.lead_id.message_post(
                body=message,
            )
        return record

    def write(self, vals):
        for rec in self:
            message = Markup("<p><b>Call Updated</b></p><ul>")
            changes = []

            if 'summary' in vals and rec.summary != vals['summary']:
                changes.append(Markup("<li><b>Summary:</b> %s → %s</li>") % (rec.summary or "N/A", vals['summary']))
            if 'date_deadline' in vals and rec.date_deadline != vals['date_deadline']:
                changes.append(
                    Markup("<li><b>Deadline:</b> %s → %s</li>") % (rec.date_deadline or "N/A", vals['date_deadline']))
            if 'user_id' in vals and rec.user_id.id != vals['user_id']:
                new_user = self.env['res.users'].browse(vals['user_id']).name
                changes.append(Markup("<li><b>Assigned to:</b> %s → %s</li>") % (rec.user_id.name or "N/A", new_user))
            if 'note' in vals and rec.note != vals['note']:
                old_note = html2plaintext(rec.note) if rec.note else "N/A"
                new_note = html2plaintext(vals['note']) if vals['note'] else "N/A"
                changes.append(Markup("<li><b>Note:</b> %s → %s</li>") % (old_note, new_note))

            if changes:
                message += Markup("").join(changes)
                message += Markup("</ul>")
                rec.lead_id.message_post(
                    body=message,
                )
        return super(CrmLeadCall, self).write(vals)
