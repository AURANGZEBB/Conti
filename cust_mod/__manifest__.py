# -*- coding: utf-8 -*-
{
    'name': 'Custom Reports',
    'version': '12.0.1.0.0',
    'category': 'Extra Tools',
    'summary': 'Module for custom reports in sale order lines',
    'sequence': '201',
    'license': 'AGPL-3',
    'author': 'AB',
    'maintainer': 'AB',
    'website': 'ab.com',
    'depends': ['base', 'fleet', 'fleet_car_workshop', 'account', 'account_accountant'],
    'demo': [],
    'data': [
        'data/sequence.xml',
        'reports/invoice_report_inherit.xml',
        'reports/receipt.xml',
        'reports/receipt_sheet.xml',
        'reports/work.xml',
        'reports/work_sheet.xml',
        'views/inherit_cost_product.xml',
    ],
    'images': ['static/description/banner.jpg','static/src/img/header.jpeg','static/src/img/footer.jpeg','static/src/img/paid.png'],
    'installable': True,
    'application': True,
    'auto_install': False,

}