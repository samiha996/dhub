from odoo import models, fields, api

class CrmLead(models.Model):
    _inherit = 'crm.lead'


    agent = fields.Many2one(
        comodel_name='res.partner',string='Agent'
    )

    study_country = fields.Many2one(
        comodel_name='res.country', string='Study Country'
    )

    is_won = fields.Boolean(string='Is Won?',default=False)
    is_lose = fields.Boolean(string='Is Lose?',default=False)


    def action_set_won_rainbowman(self):
        self.ensure_one()
        self.action_set_won()
        self.is_won = True

        message = self._get_rainbowman_message()
        if message:
            return {
                'effect': {
                    'fadeout': 'slow',
                    'message': message,
                    'img_url': '/web/image/%s/%s/image_1024' % (self.team_id.user_id._name, self.team_id.user_id.id) if self.team_id.user_id.image_1024 else '/web/static/img/smile.svg',
                    'type': 'rainbow_man',
                }
            }
        return True



    def action_set_lost(self, **additional_values):
        """ Lost semantic: probability = 0 or active = False """
        res = self.action_archive()
        self.is_lose = True
        if additional_values:
            self.write(dict(additional_values))
        return res




    