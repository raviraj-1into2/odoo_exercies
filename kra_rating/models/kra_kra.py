from odoo import api, fields, models

class KraRating(models.Model):
    _name = "kra.rating"
    _description = "Kra Rating"

    name = fields.Many2one('res.partner', string="Employee")
    month= fields.Selection([('jan','January'),('feb','February'),('march','March'),('april','April'),
                             ('may','May'),('jun','Jun'),('july','July'),('aug','August'),('sep','September'),
                             ('oct','October'),('nov','November'),('dec','December')],string="Month" , required=True)
    year_id= fields.Many2one('year.year',string="Year")
    question_ids=fields.One2many('kra.line','kra_rating_id',string="Questions")
    total_score = fields.Float(string="Total Score",compute= "_compute_total_score")

    def _compute_total_score(self):
        for rec in self:
            rec.total_score = False
            score = sum(total.final_score for total in rec.question_ids)
            print('**********************',score)
            rec.total_score = score



