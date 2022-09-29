from odoo import api, fields, models

class SaleSubscriptionTemplate(models.Model):
    _name = "sale_subscription.template"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Sale Subscription Template'

    active = fields.Boolean(string="Active", default=True)
    name = fields.Char(string="Name", tracking=True, required=True)
    description = fields.Html(string="Description")
    recurring_rule_type = fields.Selection([('daily','Daily'),('weekly','Weekly'),
                                            ('monthly','Monthly'),('yearly','Yearly')], default='monthly', string="Recurring Rule", tracking=True, required=True)
    recurring_interval = fields.Integer(string="Recurring Interval",default='1',tracking=True, required=True)
    recurring_rule_boundary = fields.Selection([('unlimited','Unlimited'),
                                                ('limited','Limited')], string="Recurring Rule Boundary",default='unlimited')
    company_id = fields.Many2one('res.company',string="Company")