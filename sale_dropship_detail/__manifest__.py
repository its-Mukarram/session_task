# -*- coding: utf-8 -*-
{
    "name": "Sale Dropship Details",
    "version": "17.0.1.0.0",
    "summary": "This module links the saleorder with purchase if dropship"
    "product exists",
    "description": """
    This module opens a wizard while confirming the sale order and if there is
    any product with dropship it links the sale order with the purchase order
    """,
    "category": "Sales",
    "website": "http://www.aktivsoftware.com",
    "author": "Aktiv Software",
    "license": "OPL-1",
    "depends": ["sale", "purchase", "stock"],
    "data": [
        "security/ir.model.access.csv",
        "views/sale_order_view.xml",
        "views/purchase_order_view.xml",
        "wizards/sale_detail_wizard_view.xml",
    ],
    "auto_install": False,
    "installable": True,
    "application": False,
}
