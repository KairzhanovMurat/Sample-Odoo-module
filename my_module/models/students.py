from odoo import models, fields, api


class Student(models.Model):
    _name = 'my_module.student'
    _description = 'some students model'

    name = fields.Char(string='Name', required=True)
    school_id = fields.Many2one('my_module.school', string='School')
    subject_ids = fields.Many2many('my_module.subject', string='Subject')
