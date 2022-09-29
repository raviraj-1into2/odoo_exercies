from odoo import api, fields, models
from odoo.exceptions import ValidationError

class HospitalAppointment(models.Model):
    _name = "year.year"
    _description = "year of employee"

    name = fields.Integer(string='Year', required=True)

    @api.constrains('name')
    def _check_name(self):
        for rec in self:
            if rec.name < 2000:
                raise ValidationError("please enter valid year")

    _sql_constraints = [
        ('unique_name', 'unique(name)', 'year must be unique!')]




