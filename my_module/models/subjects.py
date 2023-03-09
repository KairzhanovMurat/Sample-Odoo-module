from odoo import models, fields


class Subject(models.Model):
    _name = 'my_module.subject'
    _description = 'some subjects'

    name = fields.Char(string='Name', required=True)
    student_ids = fields.Many2many('my_module.student', string='Students')
    teacher_id = fields.Many2one('my_module.teacher', string='Teacher')
