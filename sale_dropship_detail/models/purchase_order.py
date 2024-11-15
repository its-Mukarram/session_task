# -*- coding: utf-8 -*-
from odoo import fields, models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    purchase_linked_sale_order_id = fields.Many2one(
        comodel_name="sale.order", string="Linked Sale Order ID", readonly=1
    )
