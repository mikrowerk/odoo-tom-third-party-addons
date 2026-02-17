from odoo import api, fields, models


class SaleOrderTemplateLine(models.Model):
    _inherit = "sale.order.template.line"

    name = fields.Text(
        string="Description",
        translate=True,
        default=""
    )

    # FIX 1: compute statt plain Float – verhindert relatedPropertyField-Fehler
    price_subtotal = fields.Float(
        string="Subtotal",
        compute="_compute_price_subtotal",
        store=True,
        default=0.0,
    )

    # === COMPUTE METHODS ===#

    @api.depends('product_uom_qty', 'display_type')
    def _compute_price_subtotal(self):
        for line in self:
            # FIX 2: Sektionen/Notizen immer auf 0 setzen
            if line.display_type:
                line.price_subtotal = 0.0
            else:
                line.price_subtotal = line.product_uom_qty  # oder deine eigene Logik

    # === CRUD METHODS ===#

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            # FIX 3: display_type direkt aus vals lesen, kein default_get als Fallback
            if vals.get('display_type'):
                vals.update(
                    product_id=False,
                    product_uom_qty=0,
                    product_uom_id=False,
                    price_subtotal=0.0,
                )
            if not vals.get('name') and vals.get('product_id'):
                vals['name'] = self._get_product_name(vals['product_id'])
        return super().create(vals_list)

    # === BUSINESS METHODS ===#

    def _prepare_order_line_values(self):
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
