import re
from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    attribute_string = fields.Char(compute='_compute_attribute_string', string='Attribute string')
    
    @api.depends('display_name')
    def _compute_attribute_string(self):
        for record in self:
            result = re.search('^.*(\(.*\))$', record.display_name)
            if result:
                attribute_string = result.group(1)
                record.attribute_string = attribute_string
            else:
                record.attribute_string = ""

    def _get_combination_info(self, combination=False, product_id=False, add_qty=1, pricelist=False, parent_combination=False, only_template=False):
        combination_info = super(ProductTemplate, self)._get_combination_info(
            combination=combination,
            product_id=product_id,
            add_qty=add_qty,
            pricelist=pricelist,
            parent_combination=parent_combination,
            only_template=only_template,
        )
        if not self.env.context.get('website_sale_product_properties'):
            return combination_info

        if combination_info['product_id']:
            product = self.env['product.product'].sudo().browse(combination_info['product_id'])
            website = self.env['website'].get_current_website()
            combination_info['all_kvs'] = product.all_kvs
        else:
            product_template = self.sudo()
            combination_info.update({
                'all_kvs': product_template.tmpl_all_kvs,
            })

        return combination_info    