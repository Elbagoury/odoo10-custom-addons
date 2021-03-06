#-*- coding:utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2011 OpenERP SA (<http://openerp.com>). All Rights Reserved
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp import models, fields, api


class ProductListPrice(models.Model):
    _name = "product.list"

    slect_prod = fields.Many2many('product.product',string="Select Product")
    slect_categ = fields.Many2one('product.category',string="Select Category")
    product = fields.Selection([
        ('all_prod','All Product'),
        ('multi_prod','Specfic or Multiple Product'),
        ('cat_wise','Category Wise'),
        ],string="Products")

class ProductListPriceWise(models.Model):
    _inherit = "product.product"    

    @api.model
    def create_report(self):
        return {
        'type': 'ir.actions.act_window',
        'name': 'Product Profile',
        'res_model': 'product.list',
        'view_type': 'form',
        'view_mode': 'form',
        'target' : 'new',
        }
    
    
