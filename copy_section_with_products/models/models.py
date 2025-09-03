# -*- coding: utf-8 -*-

from odoo import models, api, _


class SalesOrder(models.Model):
    _inherit = 'sale.order'

    @api.model
    def copy_section_with_products(self, order_id, line_id):
        order = self.env['sale.order'].browse(order_id)
        if len(order.order_line) > 0 and line_id:
            section_selected = order.order_line.filtered(lambda x: x.id == line_id)
            start_index = order.order_line.ids.index(section_selected.id) + 1
            # Find the maximum sequence number among existing lines
            max_sequence = max(order.order_line.mapped('sequence'), default=0)
            order.write({
                'order_line': [(0, 0, {
                    'name': section_selected.name + ' (copy)',
                    'product_id': section_selected.product_id.id,
                    'product_uom_qty': section_selected.product_uom_qty,
                    'price_unit': section_selected.price_unit,
                    'product_uom': section_selected.product_uom.id,
                    'product_packaging_id': section_selected.product_packaging_id.id,
                    'display_type': section_selected.display_type,
                    'tax_id': [(6, 0, section_selected.tax_id.ids)],
                    'sequence': max_sequence + 1,
                    'discount': section_selected.discount,
                    'price_subtotal': section_selected.price_subtotal,
                })]
            })
            max_sequence += 1
            for line in order.order_line[start_index:]:
                if line.display_type == 'line_section':
                    break
                order.write({
                    'order_line': [(0, 0, {
                        'name': line.name,
                        'product_id': line.product_id.id,
                        'product_uom_qty': line.product_uom_qty,
                        'price_unit': line.price_unit,
                        'product_uom': line.product_uom.id,
                        'product_packaging_id': line.product_packaging_id.id,
                        'display_type': line.display_type,
                        'tax_id': [(6, 0, line.tax_id.ids)],
                        'sequence': max_sequence + 1,
                        'discount': line.discount,
                        'price_subtotal': line.price_subtotal,
                    })]
                })
                max_sequence += 1
            return order
