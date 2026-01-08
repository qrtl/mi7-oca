# Copyright 2025 Quartile (https://www.quartile.co)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo.addons.website.controllers.form import WebsiteForm


class WebsiteForm(WebsiteForm):
    def insert_record(self, request, model, values, custom, meta=None):
        website = request.website
        if not website.specific_user_account:
            return super().insert_record(request, model, values, custom, meta)
        partner_id = values.get("partner_id")
        if not partner_id:
            return super().insert_record(request, model, values, custom, meta)
        Partner = request.env["res.partner"].sudo()
        partner = Partner.browse(partner_id)
        if not partner:
            return super().insert_record(request, model, values, custom, meta)
        email = (
            values.get("email_from")
            or values.get("partner_email")
            or values.get("email")
        )
        # Intended for newly created partners, but applies to any partner without website_id
        if not partner.website_id:
            partner.website_id = website.id
        # Intended for newly created partners, but applies to any partner without company_id
        if not partner.company_id and website.restrict_partner_to_company:
            partner.company_id = website.company_id.id
        if email and partner.website_id != website:
            domain = [
                ("email", "=", email),
                ("website_id", "=", website.id),
            ]
            if website.restrict_partner_to_company:
                domain.append(("company_id", "=", website.company_id.id))
            website_partner = Partner.search(domain, limit=1)
            if not website_partner and values.get("partner_name"):
                vals = {
                    "email": email,
                    "name": values.get("partner_name"),
                    "website_id": website.id,
                }
                if website.restrict_partner_to_company:
                    vals["company_id"] = website.company_id.id
                website_partner = Partner.create(vals)
            if website_partner:
                values["partner_id"] = website_partner.id
        return super().insert_record(request, model, values, custom, meta)
