from odoo import models, api, _, fields


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # Inheirted 'pricelist_id' field to append domain
    pricelist_id = fields.Many2one(
        comodel_name='product.pricelist',
        string="Pricelist",
        compute='_compute_pricelist_id',
        store=True, readonly=False, precompute=True, check_company=True,
        # Unrequired company
        tracking=1,
        domain="['|',"
               ""
               ""
               ""
               ""
               "('company_id', '=', False), ('company_id', '=', company_id),('start_date', '<=', date_order),'|',('end_date', '>=', date_order),('end_date', '=', False),'|',('customer_id', '=', partner_id),('customer_id', '=', False)]",
        help="If you change the pricelist, only newly added lines will be affected.")

    @api.depends('partner_id')
    def _compute_pricelist_id(self):
        """
        Computes and filters the Pricelist as per the Conditions
        """
        res = super(SaleOrder, self)._compute_pricelist_id()
        for order in self:
            if self.partner_id:
                order.pricelist_id = self.search_pricelist_ids(limit=1) or False
        return res

    def write(self, values):
        """
        Update the Prices in orderlines
        &
        Post a Message if Pricelist has changed`
        """
        old_pricelist = self.pricelist_id.name
        res = super(SaleOrder, self).write(values)
        if values.get('pricelist_id'):
            self.action_update_prices()
            self.message_post(body=_(
                f"Odoo suggested the price list '{old_pricelist}' ,but you chose '{self.pricelist_id.name}'"))
        return res

    def search_pricelist_ids(self, domain=[], limit=None):
        return self.pricelist_id.search(
            ['|', ('company_id', '=', False),
             ('company_id', '=', self.company_id.id),
             ('start_date', '<=', self.date_order), '|',
             ('end_date', '>=', self.date_order),
             ('end_date', '=', False),
             '|', ('customer_id', '=', self.partner_id.id),
             ('customer_id', '=', False)] + domain, limit=limit,
            order="id desc")

    # @api.onchange('partner_id')
    # def _onchange_pricelist_id(self):
    #     if self.partner_id:
    #         domai = [('customer_id','=',False)]
    #     return {'domain': {'pricelist_id': domai}}
