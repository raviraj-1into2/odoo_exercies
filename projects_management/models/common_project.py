from odoo import api, fields, models

class CommonProject(models.Model):
    _name = "common.project"
    _description = "Project detail"

    name=fields.Char(string="Name")
    description=fields.Text(string="Description")
    project_manager = fields.Many2one('res.users',string="project_manager")
    customer = fields.Many2one('res.partner',string="Customer")