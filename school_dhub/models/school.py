from odoo import models,fields


class School(models.Model):
    _name="school"
    
    name=fields.Char(required=True)
    code=fields.Integer()
    description=fields.Text()
    logo=fields.Binary()
    url_map=fields.Char()
    city_id=fields.Many2one('city')
    city_population=fields.Integer(related='city_id.population')
    city_description=fields.Text(related='city_id.description')
    city_image=fields.Binary(related='city_id.image')