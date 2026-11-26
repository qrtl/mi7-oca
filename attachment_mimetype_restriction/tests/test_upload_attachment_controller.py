# Copyright 2026 Quartile (https://www.quartile.co)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import http
from odoo.tests.common import HttpCase, tagged


@tagged("post_install", "-at_install")
class TestUploadAttachmentController(HttpCase):
    def test_upload_attachment_blocked_returns_error(self):
        """The parent route returns a Response, not a str, to the override."""
        self.env.company.attachment_allowed_mimetypes = "image/png"
        partner = self.env["res.partner"].create({"name": "Test Partner"})
        self.authenticate("admin", "admin")
        response = self.url_open(
            "/web/binary/upload_attachment",
            data={
                "model": "res.partner",
                "id": partner.id,
                "csrf_token": http.WebRequest.csrf_token(self),
            },
            files={"ufile": ("blocked.txt", b"text content", "text/plain")},
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("File type 'text/plain' is not allowed.", response.text)
