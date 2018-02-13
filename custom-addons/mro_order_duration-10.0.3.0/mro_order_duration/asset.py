# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo
#    Copyright (C) 2014-2016 CodUP (<http://codup.com>).
#
##############################################################################

from odoo import api, fields, models, _

class asset_asset(models.Model):
    _inherit = 'asset.asset'

    def _mroreq_count(self):
        maintenance = self.env['mro.request']
        for asset in self:
            self.mroreq_count = maintenance.search_count([('asset_id', '=', asset.id)])

    def action_view_maintenance(self):
        context={'search_default_open': 1,'search_default_asset_id': [self.id],'default_asset_id': self.id,}
        return {
            'domain': "[('asset_id','in',[" + ','.join(map(str, self.ids)) + "])]",
            'context':context,
            'name': _('Maintenance Orders'),
            'view_type': 'form',
            'view_mode': 'tree,form',
            'res_model': 'mro.order',
            'type': 'ir.actions.act_window',
            'target': 'current',
        }

    def action_view_maintenance_request(self):
        context={'search_default_open': 1,'search_default_asset_id': [self.id],'default_asset_id': self.id,}
        return {
            'domain': "[('asset_id','in',[" + ','.join(map(str, self.ids)) + "])]",
            'context':context,
            'name': _('Maintenance requests'),
            'view_type': 'form',
            'view_mode': 'tree,form',
            'res_model': 'mro.request',
            'type': 'ir.actions.act_window',
            'target': 'current',
        }

    mroreq_count = fields.Integer(compute='_mroreq_count', string='#MRO request')
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: