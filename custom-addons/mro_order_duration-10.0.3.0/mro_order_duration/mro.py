# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo
#    Copyright (C) 2013-2017 CodUP (<http://codup.com>).
#
##############################################################################

import time
from odoo import api, fields, models, _
import odoo.addons.decimal_precision as dp


class mro_order(models.Model):
    """
    add duration on Maintenance Orders, so that we can drag calendar
    """
    _inherit = 'mro.order'

    def _get_default_asset_ids(self):
        default_asset_id = self.env.context.get('default_asset_id')
        return [default_asset_id] if default_asset_id else None

    asset_id = fields.Many2one('asset.asset', 'Asset', required=True, readonly=True, states={'draft': [('readonly', False)]},default=_get_default_asset_ids)
    order_duration = fields.Float(string='Duration', store=True, default=1.0)

class mro_request(models.Model):
    _inherit = 'mro.request'

    def _get_default_asset_ids(self):
        default_asset_id = self.env.context.get('default_asset_id')
        return [default_asset_id] if default_asset_id else None

    asset_id = fields.Many2one('asset.asset', 'Asset', required=True, readonly=True, states={'draft': [('readonly', False)]},default=_get_default_asset_ids)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
