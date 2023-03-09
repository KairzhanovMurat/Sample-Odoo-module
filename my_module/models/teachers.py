from odoo import models, fields, api


class Teacher(models.Model):
    _name = 'my_module.teacher'
    _description = 'some teachers model'

    name = fields.Char(string='Name', required=True)
    salary = fields.Float(string='Salary', digits=(6, 2),
                          required=True, default=0.0)

    subject_ids = fields.One2many('my_module.subject', 'teacher_id', string='Subjects')
    school_id = fields.Many2one('my_module.school', string='School')

    total_num_of_students = fields.Integer(string='Total number of students for teacher',
                                           compute='_total_students')

    @api.depends('subject_ids.student_ids')
    def _total_students(self):
        for teacher in self:
            subjects = [subj for subj in teacher.subject_ids]
            teacher.total_num_of_students = sum(len(subj.student_ids) for subj in subjects)

