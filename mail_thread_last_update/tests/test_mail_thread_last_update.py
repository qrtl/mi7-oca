# Copyright 2025 Quartile Limited
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo.tests import common


class TestMailThreadLastUpdate(common.TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.params = cls.env["ir.config_parameter"].sudo()
        cls.message_model = cls.env["mail.message"]
        cls.partner = cls.env["res.partner"].create({"name": "Test Partner"})

    def _create_message(self, message_type="comment"):
        return self.message_model.create(
            {
                "message_type": message_type,
                "model": "res.partner",
                "res_id": self.partner.id,
                "body": "Test message",
            }
        )

    def test_update_on_target_model(self):
        self.params.set_param("mail_thread_last_update.target_models", "res.partner")
        self.params.set_param("mail_thread_last_update.message_types", "")
        self.partner.write({"last_chatter_update": False})
        message = self._create_message(message_type="comment")
        self.assertEqual(self.partner.last_chatter_update, message.date)

    def test_skip_on_non_target_model(self):
        self.params.set_param("mail_thread_last_update.target_models", "res.company")
        self.params.set_param("mail_thread_last_update.message_types", "")
        self.partner.write({"last_chatter_update": False})
        self._create_message(message_type="comment")
        self.assertFalse(self.partner.last_chatter_update)

    def test_update_on_target_message_type(self):
        self.params.set_param("mail_thread_last_update.target_models", "res.partner")
        self.params.set_param("mail_thread_last_update.message_types", "comment")
        self.partner.write({"last_chatter_update": False})
        message = self._create_message(message_type="comment")
        self.assertEqual(self.partner.last_chatter_update, message.date)

    def test_skip_on_non_target_message_type(self):
        self.params.set_param("mail_thread_last_update.target_models", "res.partner")
        self.params.set_param("mail_thread_last_update.message_types", "comment")
        self.partner.write({"last_chatter_update": False})
        self._create_message(message_type="email")
        self.assertFalse(self.partner.last_chatter_update)
