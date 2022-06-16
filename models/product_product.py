from odoo import models, fields, api

class ProductProduct(models.Model):
    _inherit = 'product.product'

    website_kvs = fields.One2many('jt.property.kv', compute='_compute_website_kvs')
    
    @api.depends('all_kvs')
    def _compute_website_kvs(self):
       self.website_kvs = self.all_kvs.filtered(lambda o: o.key_id.website)