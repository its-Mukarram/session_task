from odoo import fields, models, api


class ProductPricelist(models.Model):
    _inherit = 'product.pricelist'

    start_date = fields.Date(string="Start Date", required=True, default=fields.Date.today())
    end_date = fields.Date(string="End Date")
    customer_id = fields.Many2one(comodel_name="res.partner",
                                  string="Customer ID", )

    # @api.depends_context('from_sale')
    # def _search(self, domain=None, offset=0, limit=None, order=None):
    #     print(domain,self._context)
    #     res = super(ProductPricelist,self)._search(domain=domain)
    #     return res

    # ['|', ('company_id', '=', False), ('company_id', '=', company_id),
    #  ('start_date', '<=', date_order), '|', ('end_date', '>=', date_order),
    #  ('end_date', '=', False), '|', '|', ('customer_id', '=', partner_id),
    #  ('customer_id', '=', False)]