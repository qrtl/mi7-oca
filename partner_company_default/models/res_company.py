# Copyright 2023 Quartile Limited
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models


class ResCompany(models.Model):
    _inherit = "res.company"

    @api.model
    def create(self, vals):
        self = self.with_context(creating_from_company=True)
        company = super(ResCompany, self).create(vals)
        # add partner company_id to new company
        company.partner_id.sudo().write({"company_id": company.id})
        return company
