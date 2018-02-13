# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo
#    Copyright (C) 2013-2016 Stella Fredö.
#
##############################################################################

{
    'name': 'MRO_order_duration',
    'version': '10.0.3.0',
    'summary': 'Asset Maintenance order calendar drag',
    'description': """
Make the maintenance order can be drag on the calendar.
=====================================

Asset Maintenance, Repair and Operation.

Main Features
-------------
    * add field duration for asset Maintenance order, so that the maintenance order time duration can be drag on the calendar
    * add the web_icon for the mro application
    * add the maintenance request button in the asset form
    * the active asset id is filled when create a maintenace request from the asset form 
    * the active asset id is filled when create a maintenace order from the asset form 

Required modules:
    * asset
    * mro 
    """,
    'author': 'Stella Fredö',
    'website': '',
    'category': 'Industries',
    'sequence': 0,
    'depends': ['asset','mro'],
    'data': [
       'asset_view.xml',
       'mro_view.xml',
   ],
    'installable': True,
    'application': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
