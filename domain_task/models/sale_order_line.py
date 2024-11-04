# -*- coding: utf-8 -*-
from odoo import fields, models, api


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    # Add a field on Order Line
    pricelist_id = fields.Many2one(
        string="Price List ID", comodel_name="product.pricelist"
    )

    @api.onchange("product_template_id")
    def onchange_pricelist_id(self):
        """
        Compute the PriceList with the lowest price for the product
        """
        for line in self:
            price_lists = line.order_id.with_context(
                {"product_id": line.product_template_id.id}
            ).search_pricelist_ids()
            items = price_lists.item_ids.filtered(
                lambda product: product.product_tmpl_id.id
                == line.product_template_id.id
            ).sorted(key=lambda price: price.fixed_price)
            print("Succesfully Reached Here")
            if items:
                line.pricelist_id = items[0].pricelist_id
                line.price_unit = items[0].fixed_price
            else:
                line.pricelist_id = self.order_id.pricelist_id

    def change_pricelist(self):
        """
        change the pricelist in every orderline
        """
        for line in self:
            line.pricelist_id = self.order_id.pricelist_id
