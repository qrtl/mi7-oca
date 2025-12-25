# Copyright 2025 Quartile (https://www.quartile.co)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import api, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.model_create_multi
    def create(self, vals_list):
        website_id = self.env.context.get("website_id")
        if not website_id:
            return super().create(vals_list)
        website = self.env["website"].browse(website_id)
        if not website.specific_user_account:
            return super().create(vals_list)
        for vals in vals_list:
            if not vals.get("website_id"):
                vals["website_id"] = website.id
        return super().create(vals_list)

    @api.model
    def search(self, args, **kwargs):
        website_id = self.env.context.get("website_id")
        if not website_id:
            return super().search(args, **kwargs)
        website = self.env["website"].browse(website_id)
        if website.specific_user_account:
            args += [("website_id", "=", website_id)]
        return super().search(args, **kwargs)
