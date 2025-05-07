from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    x_student_id = fields.Char(string="Student ID", readonly=False, copy=False)

    _sql_constraints = [
        ('student_id_unique', 'unique(x_student_id)', 'Student ID must be unique.')
    ]

    @api.model
    def create(self, vals):
        if not vals.get('x_student_id'):
            vals['x_student_id'] = self._generate_student_id()
        return super(ResPartner, self).create(vals)

    def _generate_student_id(self):
        """Generate unique Student ID, skip if already used."""
        while True:
            new_student_id = self.env['ir.sequence'].next_by_code('student.id')
            # Check if already exists
            exists = self.search([('x_student_id', '=', new_student_id)], limit=1)
            if not exists:
                return new_student_id
