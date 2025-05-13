from odoo import  api, models, fields


class PatientTag(models.Model):
    _name = 'patient.tag'
    _inherit = ['mail.thread']
    _description = 'Patient Tag'

    name = fields.Char(string="Name", required=True, tracking=True)
    sequence = fields.Integer(default=10)