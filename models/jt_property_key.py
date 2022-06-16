import logging
from odoo import models, fields, api

_logger = logging.getLogger(__name__)


class PropertyKey(models.Model):
    _inherit = 'jt.property.key'

    website = fields.Boolean(string='Website', default=False, help="Show this property on the website ?")