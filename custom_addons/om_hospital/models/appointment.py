from odoo import  api, models, fields


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = "Hospital Appointment"
    _rec_names_search = ['reference', 'patient_id']
    _inherit = ['mail.thread']
    _rec_name = 'patient_id'


    reference = fields.Char(string="Reference", default='New')
    patient_id = fields.Many2one('hospital.patient', string="patient", ondelete='restrict' )
    line_ids = fields.One2many('hospital.appointment.line', 'appointment_id', string="Lines")
    appointment_date = fields.Date(string="Time")
    total_quantity = fields.Float(string="Total Quantity", compute='_compute_total_quantity', store=True)
    note = fields.Text(string="Note")
    state = fields.Selection([('draft', 'Draft'),
                              ('confirmed', 'Confirmed'),
                              ('ongoing', 'Ongoing'),
                              ('done', 'Done'),
                              ('cancel', 'Canceled')], default='draft', tracking=True)
    dob = fields.Date(string="Date of Birth", readonly=True, related='patient_id.date_of_birth', store=True)



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

    @api.depends('patient_id', 'reference')
    def _compute_display_name(self):
        for rec in self:
            rec.display_name = f'[{rec.reference}] {rec.patient_id.name}]'

    @api.depends('line_ids', 'line_ids.qty')
    def _compute_total_quantity(self):
        for rec in self:
           rec.total_quantity = sum(line.qty for line in rec.line_ids)






class HospitalAppointmentLine(models.Model):
    _name = 'hospital.appointment.line'
    _description = 'Hospital Appointment Line'

    appointment_id = fields.Many2one('hospital.appointment', string='Appointment')

    product_id = fields.Many2one('hospital.medicament', string='Medicaments')
    qty = fields.Float(string='Quantity')


