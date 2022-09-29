from odoo import api, fields, models
from odoo.exceptions import ValidationError
class HospitalPatient(models.Model):
    _name = "kra.line"
    _description = "Kra Line"

    question_id = fields.Many2one('kra.question',string="Question")
    kra_rating_id = fields.Many2one('kra.rating', 'KRA Rating')
    description = fields.Char(string="Description")
    weightage = fields.Integer(string="Weight")
    rate = fields.Integer(string="Employee Rating", default=10)
    manager_rating = fields.Integer(string="Manager Rating")
    final_score = fields.Float(string="Final Score", compute="_compute_final_score")

    @api.constrains('rate')
    def _check_rate(self):
        for rec in self:
            if rec.rate and rec.rate > 10:
                raise ValidationError("please enter valid rate ")

    def _compute_final_score(self):
        for rec in self:
            rec.final_score = False
            if rec.weightage:
                rec.final_score = rec.weightage + rec.rate + rec.manager_rating/3




