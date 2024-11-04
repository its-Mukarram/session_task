# -*- coding: utf-8 -*-
{
    "name": "Domain Task",
    "version": "17.0.1.0.0",
    "summary": "This module shows filtered Pricelist for the Customer",
    "description": """This module is takes the fields like start and end
    dates ,contact names, and filters the Pricelist according to it
    for the sale order """,
    "category": "Sales/Sales",
    "depends": ["sale"],
    "website": "http://www.aktivsoftware.com",
    "author": "Aktiv Software",
    "license": "OPL-1",
    "data": [
        "views/product_price_view.xml",
        "views/sale_order_view.xml",
    ],
    "auto_install": False,
    "installable": True,
    "application": False,
}
