# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class my_ecom_lesson1(models.Model):
#     _name = 'my_ecom_lesson1.my_ecom_lesson1'
#     _description = 'my_ecom_lesson1.my_ecom_lesson1'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

