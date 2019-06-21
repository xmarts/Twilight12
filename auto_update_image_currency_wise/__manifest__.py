# -*- coding: utf-8 -*-
# Copyright 2016 Openworx, LasLabs Inc.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    "name": "Auto Update Flag Currency Wise",
    "summary": "Auto Update Flag Currency Wise",
    "version": "12.0.1.0.2",
    "license": "LGPL-3",
    "installable": True,
    "depends": [
        'base','product','sale'
    ],
    "data": [
        'views/product_pricelist.xml',
        'views/res_currency.xml',
        'views/sale_order.xml',
    ],"images":['static/src/img/usd.png','static/src/img/mxn.png'],
}
