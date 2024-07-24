import logging
from odoo.upgrade import util


_logger = logging.getLogger(__name__)


def migrate(cr, version):

    views_to_remove = [
        'jt_product_properties_website.website_sale_product',
    ]


    for view in views_to_remove:
        _logger.info("About to remove view %s", view)
        util.remove_view(cr, xml_id=view)


