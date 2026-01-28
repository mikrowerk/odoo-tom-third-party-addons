# -*- coding: utf-8 -*-
##############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2023-TODAY Cybrosys Technologies(<https://www.cybrosys.com>).
#    Author: Mruthul Raj @cybrosys(odoo@cybrosys.com)
#
#    Fix vor sale-quotation templates, provided by Gammadata
#    Author Guenther Froestl
#    Copyright (C) 2025-TODAY Gammadata (<https://www.gammadata.de>)
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
{
    'name': 'Section Wise Subtotal',
    'version': '17.0.1.0.0',
    'category': 'Sales,Purchases',
    'summary': 'Section wise subtotal in the order line',
    'description': 'This module help you section wise subtotal in order '
                   'lines of sale and purchase'
                   'with a fix from Gammadata for sale_quotation templates',
    'author': 'Cybrosys Techno Solutions + Gammadata',
    'company': 'Cybrosys Techno Solutions + Gammadata',
    'maintainer': 'Cybrosys Techno Solutions + Gammadata',
    'website': 'https://www.cybrosys.com, https://www.gammadata.de',
    'depends': ['sale_management', 'purchase'],
    'data': [
        'views/sale_order_template_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'section_wise_subtotal/static/src/js/section_wise_subtotal.js',
        ],
    },
    'images': ['static/description/banner.jpg'],
    'license': 'AGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
}
