from odoo import api, fields, models

class SaleOrder(models.Model):
    _inherit = "sale.order"

    delivery_status = fields.Selection([('nothing','Nothing to deliver'),
                                        ('partially','Partially Deliver'),('done','Done')],compute='_compute_delivery_status', string='Delivery Status',store=True)
    # status = fields.One2many('sale.order','product_id',string='Status')

    # @api.depends('')
    def _compute_delivery_status(self):
        for rec in self:
            qty_sum = sum(order.product_uom_qty for order in rec.order_line)
            print('++++++++++',qty_sum)
            del_sum = sum(order.qty_delivered for order in rec.order_line)
            print('*********',del_sum)
            if qty_sum == del_sum:
                rec.delivery_status = "done"
            elif qty_sum > del_sum and del_sum > 0:
                rec.delivery_status = "partially"
            elif del_sum == 0:
                rec.delivery_status = "nothing"



        # for rec in self:
        #     rec.delivery_status = 'nothing'
        #     for order in rec.order_line:
        #         print('+++++++++++++', order.product_uom_qty)
        #         print('---------------', order.qty_delivered)
        #         if order.product_uom_qty == order.qty_delivered:
        #             rec.delivery_status = 'done'
        #         # elif order.product_uom_qty != order.qty_delivered:
        #         #     rec.delivery_status = 'partially'

