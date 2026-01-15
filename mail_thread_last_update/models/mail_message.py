# Copyright 2025 Quartile (https://www.quartile.co)

from odoo import api, fields, models


class MailMessage(models.Model):
    _inherit = "mail.message"

    @api.model_create_multi
    def create(self, vals_list):
        messages = super().create(vals_list)
        messages._update_last_chatter_update()
        return messages

    def _update_last_chatter_update(self):
        params = self.env["ir.config_parameter"].sudo()
        models_value = (params.get_param("mail_thread_last_update.target_models") or "").strip()
        types_value = (params.get_param("mail_thread_last_update.message_types") or "").strip()

        target_models = {item.strip() for item in models_value.split(",") if item.strip()}
        message_types = {item.strip() for item in types_value.split(",") if item.strip()}

        for message in self:
            is_target = (
                message.model
                and message.res_id
                and (not target_models or message.model in target_models)
                and (not message_types or message.message_type in message_types)
            )
            if not is_target:
                continue

            record = self.env[message.model].browse(message.res_id)
            if record.exists() and hasattr(record, "last_chatter_update"):
                record.sudo().write({
                    "last_chatter_update": message.date or fields.Datetime.now(),
                })
