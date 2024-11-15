# -*- coding: utf-8 -*-
from odoo.fields import Command

from odoo import fields, models


class SaleDetailWizard(models.Model):
    _name = "sale.detail.wizard"

    partner_id = fields.Many2one(comodel_name="res.partner", string="Partner ID")
    delivery_date = fields.Date(string="Delivery Date")
    sale_notes = fields.Text(string="Sales Notes", required=False)
    is_dropship = fields.Boolean(string="Dropship", readonly=1)
    product_ids = fields.One2many(
        comodel_name="sale.product",
        inverse_name="wizard_id",
        string="Product Id",
        required=False,
    )

    def action_confirm(self):
        """
        Calls the Action confirm of Sale Order
        """
        sale_order = self.env["sale.order"].browse(self.env.context.get("active_id"))
        sale_order.write(
            {
                "partner_id": self.partner_id,
                "commitment_date": self.delivery_date,
                "note": self.sale_notes,
                "order_line": [Command.clear()]
                + list(
                    map(
                        lambda line: (
                            Command.create(
                                {
                                    "product_id": line.product_id.id,
                                    "product_uom_qty": line.quantity,
                                }
                            )
                        ),
                        self.product_ids,
                    )
                ),
            }
        )
        sale_order.with_context({"from_wizard": True}).action_confirm()


class SaleProduct(models.Model):
    _name = "sale.product"

    wizard_id = fields.Many2one(
        comodel_name="sale.detail.wizard",
        string="Wizard Id",
        required=False,
    )
    product_id = fields.Many2one(
        comodel_name="product.product",
        string="Product ID",
        required=False,
    )
    quantity = fields.Float(
        string="Quantity",
        required=False,
    )
