# -*- coding: utf-8 -*-
# Copyright 2019 Creu Blanca
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    'name': "Base report csv",

    'summary': "Base module to create csv report",
    'author': 'Creu Blanca,'
              'ACSONE SA/NV,'
              'Odoo Community Association (OCA)',
    'website': "https://github.com/oca/reporting-engine",
    'category': 'Reporting',
    'version': '10.0.1.0.0',
    'license': 'AGPL-3',
    'depends': [
        'report',
    ],
    'external_dependencies': {
        'python': ['unicodecsv']
    },
    'data': [
        'views/webclient_templates.xml',
    ],
    'demo': [
        'demo/report.xml',
    ],
    'installable': True,
}