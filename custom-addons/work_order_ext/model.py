# -*- coding: utf-8 -*- 
from odoo import models, fields, api

class WokrOrder(models.Model):
    _inherit = 'mrp.production'

    custome_po = fields.Char(string="Customer Po#")
    style_no = fields.Char(string="Style No")
    vessal = fields.Date(string="Vessal Date")
    plan_qty = fields.Char(string="Plan Qty")
    week = fields.Integer(string="Week")

    remarks = fields.Text(string="Remarks")

    destination = fields.Many2one('country.countries',string="Destination")
    unit = fields.Many2one('purchase.access.issue',string="Unit")
    buyer = fields.Many2one('res.partner',string="Buyer")
    production_id =fields.One2many('production.tree','production_tree')

class WokrOrder(models.Model):
    _name = 'production.tree'

    accessories = fields.Many2one('product.template',string="Accessories")
    required_quantity = fields.Char(string="Required Quantity")
    purchased = fields.Char(string="Purchased")
    production_tree  =fields.Many2one('mrp.production')

class Countries(models.Model):
    _name = 'country.countries'
    _rec_name = 'country'

    country = fields.Char(string="Name")