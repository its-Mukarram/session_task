# -*- coding: utf-8 -*-
from odoo.fields import Command

from odoo import fields, models, _


class SaleOrder(models.Model):
    _inherit = "sale.order"

    sale_linked_purchase_order_id = fields.Many2one(
        comodel_name="purchase.order", string="Linked Purchase Order ID"
    )

    def action_confirm(self):
        """
        At the action_confirm of sale order checks if its coming from wizard
        using context
        """
        if not self._context.get("from_wizard"):
            return {
                "name": _("Dropship Details"),
                "type": "ir.actions.act_window",
                "res_model": "sale.detail.wizard",
                "view_mode": "form",
                "view_id": self.env.ref("sale_dropship_detail.wizard_form_view").id,
                "target": "new",
                "context": {
                    "default_partner_id": self.partner_id.id,
                    "default_product_ids": list(
                        map(
                            lambda line: (
                                Command.create(
                                    {
                                        "product_id": line.product_id.id,
                                        "quantity": line.product_uom_qty,
                                    }
                                )
                            ),
                            self.order_line,
                        )
                    ),
                    "default_is_dropship": (
                        True
                        if any(
                            self.env.ref(
                                "stock_dropshipping.route_drop_shipping",
                                raise_if_not_found=False,
                            ).id
                            in product.route_ids.ids
                            for product in self.order_line.product_id
                        )
                        else False
                    ),
                },
            }
        res = super(SaleOrder, self).action_confirm()
        self.sale_linked_purchase_order_id = self.order_line.purchase_line_ids.order_id
        self.order_line.purchase_line_ids.order_id.purchase_linked_sale_order_id = (
            self.id
        )
        return res
