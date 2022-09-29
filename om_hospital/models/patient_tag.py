from odoo import api, fields, models

class HospitalAppointment(models.Model):
    _name = "patient.tag"
    _description = "Patient Tag"

    name =  fields.Char(string="Name")
    active = fields.Boolean(string="Active", default=True)
    color= fields.Integer(string="Color")
    sequence= fields.Integer(string="Sequence")

    _sql_constraints = [
        ('unique_tag_name', 'unique (name,active)', 'Name must be unique!'),
        ('check_sequence', 'check(sequence > 0)', 'Sequence must be non zero positive number !')
    ]