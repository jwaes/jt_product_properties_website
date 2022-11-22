# -*- coding: utf-8 -*-
{
    'name': "jt_product_properties_website",

    'summary': "Product properties website",

    'description': "",

    'author': "jaco tech",
    'website': "https://jaco.tech",
    "license": "AGPL-3",


    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.12',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'website_sale_stock',
        'jt_product_properties',
        ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/jt_property_key.xml',
        'views/website_sale_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'assets': {
        'web.assets_frontend': [
            'jt_product_properties_website/static/src/js/**/*',
        ],
    },    
}
