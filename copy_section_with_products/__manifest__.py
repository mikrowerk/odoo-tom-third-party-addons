# -*- coding: utf-8 -*-
{
    'name': "Copy Section With Products",

    'summary': """
        Copy Section With Products""",

    'description': """
        this module copy section with products and it available in sales order and rental order
    """,
    'author': "Cloudmen",
    'website': "https://www.cloudmen.ae",
    "license": "OPL-1",
    'category': 'sales',
    "version": "18.0.1.0.0",
    'module_type': 'official',
    'depends': ['base', 'sale', 'account'],
    'contributors': "Youssef Mohamed <yousef@cloudmen.com>",
    # always loaded
    'data': [
    ],
    'assets': {
        'web.assets_backend': [
            'copy_section_with_products/static/src/js/section_and_note_fields_backend.js',
            'copy_section_with_products/static/src/xml/section_and_note_fields_backend.xml',
        ],
    },
    'images': ['static/description/banner.png'],

}
