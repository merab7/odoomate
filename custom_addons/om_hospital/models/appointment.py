from odoo import  api, models, fields


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = "Hospital Appointment"
    _inherit = ['mail.thread']
    _rec_name = 'patient_id'

    reference = fields.Char(string="Reference", default='New')
    patient_id = fields.Many2one('hospital.patient', string="patient")
    line_ids = fields.One2many('hospital.appointment.line', 'appointment_id', string="Lines")
    appointment_date = fields.Date(string="Time")
    note = fields.Text(string="Note")
    state = fields.Selection([('draft', 'Draft'),
                              ('confirmed', 'Confirmed'),
                              ('ongoing', 'Ongoing'),
                              ('done', 'Done'),
                              ('cancel', 'Canceled')], default='draft', tracking=True)

    @api.model_create_multi
    def create(self, vals_list):
         for vals in vals_list:
             if not vals.get('reference') or vals['reference']=='New':
                 vals['reference'] = self.env['ir.sequence'].next_by_code('hospital.appointment')
         return super().create(vals_list)

    def action_confirm(self):
        """
        set appointment state to confirmed
        """
        for rec in self:
            rec.state='confirmed'


    def action_ongoing(self):
        """
        set appointment state to ongoing
        """
        for rec in self:
            rec.state='ongoing'


    def action_done(self):
        """
        set appointment state to done
        """
        for rec in self:
            rec.state='done'


    def action_cancel(self):
        """
        set appointment state to cancel
        """
        for rec in self:
           rec.state='cancel'


    def action_undo(self):
        """
        set appointment state to draft
        """
        for rec in self:
            rec.state = 'draft'



class HospitalAppointmentLine(models.Model):
    _name = 'hospital.appointment.line'
    _description = 'Hospital Appointment Line'

    appointment_id = fields.Many2one('hospital.appointment', string='Appointment')

    product_id = fields.Many2one('product.product', string='Product')
    qty = fields.Float(string='Quantity')


