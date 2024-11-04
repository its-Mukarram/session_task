from odoo import fields, models


class ProductPricelist(models.Model):
    _inherit = "product.pricelist"

    start_date = fields.Date(
        string="Start Date", required=True, default=fields.Date.today()
    )
    end_date = fields.Date(string="End Date")
    customer_id = fields.Many2one(
        comodel_name="res.partner",
        string="Customer ID",
    )

    def _search(self, domain=[], offset=0, limit=None, order=None):
        """
        To search specific pricelist for the customer
        """
        if self.env.context.get("date_order"):
            domain = self._create_domain(domain)
        return super(ProductPricelist, self)._search(
            domain=domain, limit=limit, order=order, offset=offset
        )

    def _create_domain(self, domain=[]):
        """
        customizing the domain according to the requirement
        """
        if self.env.context.get("company_id"):
            domain += [
                (
                    "company_id",
                    "in",
                    [self.env.context.get("company_id"), False],
                )
            ]
        if self.env.context.get("partner_id"):
            domain += [
                (
                    "customer_id",
                    "in",
                    [self.env.context.get("partner_id"), False],
                ),
                ("start_date", "<=", self.env.context.get("date_order")),
                "|",
                ("end_date", ">=", self.env.context.get("date_order")),
                ("end_date", "=", False),
            ]
            if self.env.context.get("product_id"):
                domain += [
                    (
                        "item_ids.product_tmpl_id",
                        "=",
                        self.env.context.get("product_id"),
                    )
                ]
        return domain
