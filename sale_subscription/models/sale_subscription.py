from odoo import api, fields, models
from datetime import datetime

class SaleSubscription(models.Model):
    _name = "sale.subscription"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Sale Subscription'

    name = fields.Char(string="Name", copy=False, tracking=True)
    reference = fields.Char(string="Reference",copy=False)

    partner_id = fields.Many2one('res.partner', string="Partner", tracking=True, required=True)
    partner_invoice_id = fields.Many2one('res.partner', string="Partner Invoice", required=True)
    partner_shipping_id = fields.Many2one('res.partner', string="Partner Shipping", required=True)

    date_start = fields.Datetime(string="Start Date", default=datetime.today(),copy=False, tracking=True)
    date_end = fields.Datetime(string="End Date",copy=False,tracking=True)

    currency_id = fields.Many2one('res.currency', string="Currency")
    health = fields.Selection([('normal','Normal'), ('good','Good'), ('bad','Bad')], string="Health", default='normal')
    to_renew = fields.Boolean(string="To Renew")

    template_id = fields.Many2one('sale_subscription.template', string="Template", required=True)
    recurring_rule_type = fields.Selection([('daily', 'Daily'), ('weekly', 'Weekly'),
                                            ('monthly', 'Monthly'), ('yearly', 'Yearly')], default='monthly',
                                           string="Recurring Rule", related='template_id.recurring_rule_type')
    recurring_interval = fields.Integer(string="Recurring Interval", related='template_id.recurring_interval')
    company_id = fields.Many2one('res.company',string="Company")
    stage = fields.Selection([('draft','Draft'), ('inprogress','Inprogress'),
                              ('closed','Closed')], default='draft' ,string="Stage",copy=False,tracking=True)


# if del_sum == 0:
#     rec.delivery_status = "nothing"
# elif qty_sum > del_sum:
#     rec.delivery_status = "partially"
# else:
#     rec.delivery_status = "done"