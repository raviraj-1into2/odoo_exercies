from odoo import api, fields, models

class KraQuestion(models.Model):
    _name = "kra.question"
    _description = "Questions"

    name = fields.Text(string="Question", required=True)

    _sql_constraints = [
        ('unique_name', 'unique(name)', 'Question must be unique!')]

