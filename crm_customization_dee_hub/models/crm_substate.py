from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class CrmSubState(models.Model):
    _name = 'crm.substate'

    name = fields.Char(
        required=True
    )
    