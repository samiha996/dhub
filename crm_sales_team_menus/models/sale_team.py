from odoo import models, fields, api

class SalesTeam(models.Model):
    _inherit = 'crm.team'

    @api.model
    def create(self, vals):
        team = super(SalesTeam, self).create(vals)
        menu_root = self.env.ref('crm.crm_menu_root')

        
        # Create a group for the Sales Team
        group = self.env['res.groups'].create({
            'name': f"Sales Team: {team.name}",
            'category_id': self.env.ref('base.module_category_sales').id
        })
        
        if team.member_ids:
            group.users = [(6, 0, team.member_ids.ids)]
            
        # Create a menu and action dynamically for the new team
        action = self.env['ir.actions.act_window'].create({
            'name': team.name + " Opportunities",
            'res_model': 'crm.lead',
            'view_mode': 'tree,form',
            'domain': "[('type', '=', 'opportunity'), ('team_id', '=', %d)]" % team.id,
            'context': "{'search_default_team_id': %d, 'default_team_id': %d, 'default_type': 'opportunity'}" % (team.id, team.id),
        })

        self.env['ir.ui.menu'].create({
            'name': team.name,
            'parent_id': menu_root.id,
            'action': "ir.actions.act_window,%d" % action.id,
            'sequence': 10,
            'groups_id': [(6, 0, [group.id])]
        })

        return team
    
    def write(self, vals):
        res = super(SalesTeam, self).write(vals)

        for team in self:
            # Find the group associated with this Sales Team
            group = self.env['res.groups'].search([('name', '=', f"Sales Team: {team.name}")], limit=1)

            if group:
                # Update group members
                group.users = [(6, 0, team.member_ids.ids)]

        return res

    
    def unlink(self):
        for team in self:
            menu = self.env['ir.ui.menu'].search([('name', '=', team.name)])
            menu.unlink()
        return super(SalesTeam, self).unlink()

