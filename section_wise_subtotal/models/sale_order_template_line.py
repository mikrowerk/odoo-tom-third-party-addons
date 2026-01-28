# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class SaleOrderTemplateLine(models.Model):
    _inherit = "sale.order.template.line"

    name = fields.Text(
        string="Description",
        translate=True,
        default=""
    )

    price_subtotal = fields.Float("Subtotal", default=0.0)

    # === CRUD METHODS ===#

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('display_type', self.default_get(['display_type'])['display_type']):
                vals.update(product_id=False, product_uom_qty=0, product_uom_id=False, price_subtotal=0.0)
            if not vals.get('name', False) and vals.get('product_id', False):
                vals.update(name=self._get_product_name(vals['product_id']))
        return super().create(vals_list)

    # === BUSINESS METHODS ===#

    def _prepare_order_line_values(self):
        """ Give the values to create the corresponding order line.

        :return: `sale.order.line` create values
        :rtype: dict
        """
        self.ensure_one()
        return {
            'display_type': self.display_type,
            'name': self.name if self.name else self._get_product_name(self.product_id.id),
            'product_id': self.product_id.id,
            'product_uom_qty': self.product_uom_qty,
            'product_uom': self.product_uom_id.id,
            'sequence': self.sequence,
        }

    def _get_product_name(self, product_id):
        product = self.env['product.product'].browse(product_id)
        return product.name if product else ""
