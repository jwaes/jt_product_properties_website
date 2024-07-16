import re
from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    attribute_string = fields.Char(
        compute='_compute_attribute_string', string='Attribute string')

    @api.depends('display_name')
    def _compute_attribute_string(self):
        for record in self:
            result = re.search(r'^.*(\(.*\))$', record.display_name)
            if result:
                attribute_string = result.group(1)
                record.attribute_string = attribute_string
            else:
                record.attribute_string = ""


    def _get_additionnal_combination_info(self, product_or_template, quantity, date, website):
        res = super()._get_additionnal_combination_info(product_or_template, quantity, date, website)

        if not self.env.context.get('website_sale_product_properties'):
            return res

        product_or_template = product_or_template.sudo()
        # res.update({
        #     # 'product_type': product_or_template.type,
        #     # 'allow_out_of_stock_order': product_or_template.allow_out_of_stock_order,
        #     # 'available_threshold': product_or_template.available_threshold,
        # })
        if product_or_template.is_product_variant:
            product = product_or_template
            res.update({
                'all_kvs':  product.all_kvs,
            })
        else:
            template = product_or_template
            res.update({
                'all_kvs':  template.tmpl_all_kvs,
            })

        return res

    # def _get_combination_info(
    #         self, combination=False, product_id=False, add_qty=1.0,
    #         parent_combination=False, only_template=False, ):
            
    #     combination_info = super(ProductTemplate, self)._get_combination_info(
    #         combination=combination,
    #         product_id=product_id,
    #         add_qty=add_qty,
    #         parent_combination=parent_combination,
    #         only_template=only_template,
    #     )

    #     if not self.env.context.get('website_sale_product_properties'):
    #         return combination_info

    #     if combination_info['product_id']:
    #         product = self.env['product.product'].sudo().browse(
    #             combination_info['product_id'])
    #         # website = self.env['website'].get_current_website()
    #         combination_info['all_kvs'] = product.all_kvs
    #     else:
    #         product_template = self.sudo()
    #         combination_info.update({
    #             'all_kvs': product_template.tmpl_all_kvs,
    #         })

    #     return combination_info
