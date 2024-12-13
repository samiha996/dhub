from odoo import models, fields,api
from odoo.exceptions import ValidationError

class ProductTemplate(models.Model):
    _inherit = "product.template"
    
    min_age=fields.Integer(string="Minimum Age")
    
    start_date=fields.Date(string="Start Date")
    day_name = fields.Char(string="Day Name", compute="_compute_day_name", store=True)

    study_time=fields.Selection([('morning','Morning'),('night','Night')],
                                default='morning', string="Study Time")
    
    max_students_class=fields.Integer()
    
    lesson_per_week=fields.Integer()
    hours_per_week=fields.Integer()
    avg_students_class=fields.Integer()
    required_level=fields.Selection([('beginner','Beginner'),
                                     ('intermediate','Intermediate'),
                                     ('advanced','Advanced')])
    
    school_id=fields.Many2one('school',string="School")
    school_description=fields.Text(related="school_id.description",string="Description")
    school_url=fields.Char(related="school_id.url_map", string="Location")
    school_logo=fields.Binary(related='school_id.logo')
    
    
    @api.constrains('min_age','max_students_class','avg_students_class')
    def _check_negative(self):
        for rec in self:
            if rec.min_age <0 or rec.max_students_class <0 or rec.avg_students_class<0:
                raise ValidationError("You entered a Negative Number")
            
    @api.constrains('lesson_per_week','hours_per_week')
    def _check_negative_lesson(self):
        for rec in self:
            if rec.lesson_per_week <0 or rec.hours_per_week <0 :
                raise ValidationError("You entered a Negative Number")
    
    @api.depends('start_date')
    def _compute_day_name(self):
        for rec in self:
            if rec.start_date:
                # Convert the date to a day name (e.g., Mon, Tue)
                rec.day_name = rec.start_date.strftime('%a')
            else:
                rec.day_name = False
    
    
    