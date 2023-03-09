from odoo import models, fields, api


class School(models.Model):
    _name = 'my_module.school'
    _description = 'some schools'

    name = fields.Char(string='Name', required=True)

    student_ids = fields.One2many('my_module.student', 'school_id', string='Students')
    teacher_ids = fields.One2many('my_module.teacher', 'school_id', string='Teachers')

    avg_teacher_salary = fields.Float(compute='_avg_salary', string='avg salary among teachers for school',
                                      digits=(6, 2), default=0.0, store=True)

    @api.depends('teacher_ids.salary')
    def _avg_salary(self):
        for school in self:
            teachers = school.teacher_ids
            if teachers:
                salary = [teach.salary for teach in teachers]
                school.avg_teacher_salary = sum(salary) / len(salary)
