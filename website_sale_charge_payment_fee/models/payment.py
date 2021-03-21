# -*- coding: utf-8 -*-
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import models, fields, api
import odoo.addons.decimal_precision as dp
import logging
_logger = logging.getLogger(__name__)


class PaymentAcquirer(models.Model):
    _inherit = 'payment.acquirer'

    charge_fee = fields.Boolean(
        "Fee charged to customer",
        help="An extra fee line will be added to online order when using this "
             "payment method")
    charge_fee_description = fields.Text("Fee Description")
    charge_fee_product_id = fields.Many2one(
        'product.product', string="Fee Product")
    charge_fee_tax_ids = fields.Many2many(
        'account.tax', string='Taxes')
    charge_fee_fixed_price = fields.Float(
        'Fixed Price', digits=dp.get_precision('Product Price'))
    charge_fee_percentage = fields.Float(
        'Percentage', help="Percentage applied to order total")
    charge_fee_type = fields.Selection([
        ('fixed', 'Fixed'),
        ('percentage', 'Percentage'),
    ], string="Computation type", default='fixed')

    @api.onchange("charge_fee_product_id")
    def onchange_charge_fee_product_id(self):
        if self.charge_fee_product_id:
            self.charge_fee_description = self.charge_fee_product_id.name


class TransferPaymentTransaction(models.Model):
    _inherit = 'payment.transaction'

    def _transfer_form_validate(self, data):
        if self.acquirer_id.provider == 'transfer' and self.acquirer_id.auto_confirm == 'generate_and_pay_invoice':
            _logger.info('Validated transfer payment for tx %s: set as done' % (self.reference))
            if self.sale_order_id:
                tx = self
                self.sale_order_id.sudo().update_fee_line(tx)
            return self.write({'state': 'done'})
        if self.acquirer_id.provider == 'transfer' and self.acquirer_id.auto_confirm == 'confirm_so':
            _logger.info('Validated transfer payment for tx %s: set as done' % (self.reference))
            if self.sale_order_id:
                tx = self
                self.sale_order_id.sudo().update_fee_line(tx)
            return self.write({'state': 'done'})
        _logger.info('Validated transfer payment for tx %s: set as pending' % (self.reference))
        return self.write({'state': 'pending'})

