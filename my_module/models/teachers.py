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
    avg_students = fields.Integer(string='Average amount of students in a subject for teacher',
                                  compute='_avg_students')

    @api.depends('subject_ids.student_ids')
    def _total_students(self):
        for teacher in self:
            subjects = teacher.subject_ids
            if subjects:
                teacher.total_num_of_students = sum(len(subj.student_ids) for subj in subjects)
            else:
                teacher.total_num_of_students = 0

    @api.depends('total_num_of_students', 'subject_ids.student_ids')
    def _avg_students(self):
        for teacher in self:
            subjects = teacher.subject_ids
            if subjects:
                teacher.avg_students = teacher.total_num_of_students / len(subjects)
            else:
                teacher.avg_students = 0


