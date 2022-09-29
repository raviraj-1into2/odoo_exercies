from datetime import date
from odoo import api, fields, models
from odoo.exceptions import ValidationError

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = "Hospital Patient"

    name = fields.Char(string="Name", tracking=True)
    date_of_birth = fields.Date(string="Date Of Birth")
    ref = fields.Char(string="Reference")
    age = fields.Integer(string="Age", compute='_compute_age', tracking=True)
    gender = fields.Selection([('male','Male'),('female','Female')],string="Gender",tracking=True)
    appointment_id = fields.Many2one('hospital.appointment',string="Appointments")
    appointment_count = fields.Integer(string="Appointment Count", compute= '_compute_appointment_count', store=True)
    apoointment_ids = fields.One2many('hospital.appointment', 'patient_id',string="Appointments")
    @api.depends('apoointment_ids')
    def _compute_appointment_count(self):
        for rec in self:
            rec.appointment_count = self.env['hospital.appointment'].search_count([('patient_id', '=', rec.id)])

    @api.constrains('date_of_birth')
    def _check_date_of_birth(self):
        for rec in self:
            if rec.date_of_birth and rec.date_of_birth >= fields.Date.today():
                raise ValidationError("The entered date of birth is not acceptable! ")
    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 0
