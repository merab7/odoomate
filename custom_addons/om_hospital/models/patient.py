from odoo import  api, models, fields


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Patient Master'

    name = fields.Char(string="Name", required=True)
    date_of_birth = fields.Date(string='DOB', required=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender", required=True)