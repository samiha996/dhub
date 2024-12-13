from odoo import models,fields

class City(models.Model):
    _name='city'
    
    name=fields.Char(string="Name")
    population=fields.Integer(string="Population")
    description=fields.Text(string="Description")
    image=fields.Binary(string="Image")