from odoo import models, api, exceptions, _

class MailMessage(models.Model):
    _inherit = "mail.message"

    def write(self, vals):
        if self.env.user.has_group('base.group_system'):
            return super(MailMessage, self).write(vals)
        else:
            raise exceptions.UserError(_("You are not allowed to edit or delete log notes."))

