from odoo import api, models, fields, _
from odoo.exceptions import ValidationError


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



    @api.ondelete(at_uninstall=True)
    def _check_if_patient_is_linked_to_appointment(self):
            """
            if patient is linked to appointment then do not delete it
            """
            domain = [('patient_id', '=', self.id)]
            for rec in self:
                appointments = self.env['hospital.appointment'].search(domain)
                if appointments:
                    from odoo.exceptions import UserError
                    raise ValidationError(_("Patient is linked to appointment. Please delete the appointment first."))


    # def unlink(self):
    #     """
    #     if patient is linked to appointment then do not delete it
    #     """
    #     domain = [('patient_id', '=', self.id)]
    #     for rec in self:
    #         appointments = self.env['hospital.appointment'].search(domain)
    #         if appointments:
    #             from odoo.exceptions import UserError
    #             raise ValidationError(_("Patient is linked to appointment. Please delete the appointment first."))
    #     return super().unlink()