import re
from odoo import models, fields, api

class ProductProduct(models.Model):
    _inherit = 'product.product'

    website_kvs = fields.One2many('jt.property.kv', compute='_compute_website_kvs')
    
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

    @api.depends('all_kvs')
    def _compute_website_kvs(self):
       self.website_kvs = self.all_kvs.filtered(lambda o: o.key_id.website)