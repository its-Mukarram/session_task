from odoo import fields, models, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    # partner_id = fields.Many2one(related='order_id.partner_id',string='Partner Id')
    # date_order = fields.Datetime(related='order_id.date_order', string='Order Date')
    #Add a field on Order Line
    pricelist_id = fields.Many2one(compute='_compute_pricelist_id',
                                   readonly = False,
                                   string="Price List ID",
                                   domain="['|', ('company_id', '=', False), ('company_id', '=', company_id),('start_date', '<=', parent.date_order),'|',('end_date', '>=', parent.date_order),('end_date', '=', False),'|',('customer_id', '=', parent.partner_id),('customer_id', '=', False),('item_ids.product_tmpl_id', '=', product_template_id)]",
                                   comodel_name='product.pricelist')

    @api.depends('product_template_id')
    def _compute_pricelist_id(self):
        """
        Compute the PriceList with the lowest price for the product
        """
        for line in self:

            price_lists = line.order_id.search_pricelist_ids(domain=[('item_ids.product_tmpl_id', '=', line.product_template_id.id)])

            items = price_lists.item_ids.filtered(lambda
                                                      product: product.product_tmpl_id.id == line.product_template_id.id).sorted(
                key=lambda price: price.fixed_price)
            if items:
                line.pricelist_id = items[0].pricelist_id
                line.price_unit = items[0].fixed_price
            else:
                line.pricelist_id = self.order_id.pricelist_id

