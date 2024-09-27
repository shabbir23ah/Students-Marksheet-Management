from odoo import fields, models


class StudentMarksheetManagementSystem(models.Model):
    _name = 'student.marksheet'
    _description = 'Student Marksheet'

    name = fields.Char(string='Name')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    date = fields.Datetime(default=lambda *args, **kwargs: fields.Datetime.now())
    subject = fields.Char(string='Subject')
    mark = fields.Float(string='Mark')
    remark = fields.Char(string='Remark')