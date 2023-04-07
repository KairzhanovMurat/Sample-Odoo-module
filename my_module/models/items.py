

from odoo import models, fields, api


class Item(models.Model):
    _name = 'my_module.item'
    _description = 'shop items'

    name = fields.Char(string='Name of the product', size=30, required=True)
    description = fields.Text(string='Short description', size=100)
    price = fields.Float(required=True, string='Price of the product')
    image = fields.Image(string='Image of the product',  max_width=300, max_height=300)
    type = fields.Selection([
        ('mobile', 'Mobile'),
        ('laptop', 'Laptop'),
        ('other', 'Other')
    ], string='Product type', default='other')



