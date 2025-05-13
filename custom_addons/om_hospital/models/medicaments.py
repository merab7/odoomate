from odoo import  api, models, fields


class Medicaments(models.Model):
    _name = 'hospital.medicament'
    _description = 'List of Medicaments'

    name = fields.Char(string="Name", required=True, tracking=True)

