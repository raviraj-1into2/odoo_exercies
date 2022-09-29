from odoo import api, fields, models

class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Appointment"
    _rec_name = 'patient_id'

    patient_id = fields.Many2one('hospital.patient', string="Patient")
    gender = fields.Selection(related='patient_id.gender')
    appointment_time = fields.Datetime(string="Appointment Time")
    booking_date = fields.Date(string="Booking Date")
    ref = fields.Char(string="Reference", help="Reference of the patient from patient record")
    prescription = fields.Html(string="Prescription")
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'low'),
        ('2', 'high'),
        ('3', 'very high')], string="Priority")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_consultation', 'In Consultation'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')], default='draft', string="Status", required=True)
    doctor_id= fields.Many2one('res.users',string="Docter")
    pharmacy_line_ids = fields.One2many('appointment.pharmacy.lines','appointment_id',string="Pharmacy")
    hide_sales_price = fields.Boolean(string="Hide Sales Price")
    @api.onchange('patient_id')
    def onchange_patient_id(self):
        self.ref = self.patient_id.ref

    def action_test(self):
        print("Button clicked!!!!!!!!!!")
        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'click Successfully',
                'type': 'rainbow_man',
            }
        }

    def action_in_consultation(self):
        for rec in self:
            rec.state = "in_consultation"

    def action_done(self):
        for rec in self:
            rec.state = "done"

    def action_cancel(self):
        for rec in self:
            rec.state = "cancel"

    def action_draft(self):
        for rec in self:
            rec.state = "draft"

class AppointmentPharmacyLines(models.Model):
    _name = "appointment.pharmacy.lines"
    _description= "Appointment Pharmacy Lines"

    product_id = fields.Many2one('product.product', required=True)
    price_unit = fields.Float(string="Sales Price")
    qty = fields.Integer(string='Quantity',default=1)
    appointment_id = fields.Many2one('hospital.appointment', string="Appointment")
    sub_total= fields.Float(string="Sub Total", compute='_compute_sub_total')
    total = fields.Integer(string="Total",compute='_compute_total')

    @api.onchange('product_id')
    def onchange_product_id(self):
        self.price_unit = self.product_id.lst_price

    @api.depends('price_unit','qty')
    def _compute_sub_total(self):
        for rec in self:
            rec.sub_total=False
            if rec.price_unit:
                rec.sub_total = rec.price_unit * rec.qty

