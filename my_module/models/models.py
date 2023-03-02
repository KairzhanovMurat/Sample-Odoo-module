

from odoo import models, fields


class my_module(models.Model):
    _name = 'my_module.my_module'
    _description = 'my_module.my_module'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    extra_field1 = fields.Char(string='New fiield')
    one_more_field = fields.Char(string='Another one')
    date_field = fields.Date(string='Date field')



