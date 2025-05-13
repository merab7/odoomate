from odoo import  api, models, fields


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread']
    _description = 'Patient Master'

    name = fields.Char(
        string="Name", required=True, tracking=True
    )
    date_of_birth = fields.Date(string='DOB', required=True, tracking=True )
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')],
                              string="Gender",
                              required=True, tracking=True)
    tag_ids = fields.Many2many('patient.tag',
                               'patient_tag_relation',
                               'patient_id',
                               'tag_id',
                               string="Tags")
