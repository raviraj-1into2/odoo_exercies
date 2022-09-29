from odoo import api, fields, models

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Property"

    title_id = fields.Char(string="Title")
    description = fields.Char(string="Description")
    post_cost=fields.Integer(string="Postcode",readonly=True)
    expected_price=fields.Float(string="Expected Price")
    bedrooms=fields.Integer(string="Bedrooms", default=2)
    facades=fields.Integer(string="facades")
    garden=fields.Boolean(string="Garden")
    garden_orientation=fields.Char(string="Garden Orientaion", readonly=True)
    active=fields.Boolean(string="Active")
    available_form=fields.Date(string="Available Form")
    selling_price=fields.Float(string="Selling Price")
    living_area=fields.Float(string="Living Area(sqm)")
    garage=fields.Boolean(string="Garage")
    garden_area=fields.Integer(string="Garden Area")
    status=fields.Selection([('new','New'), ( 'received','Offer Received'),
                              ('accepted','Offer Accepted')],string="Status")

