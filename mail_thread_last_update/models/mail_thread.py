# Copyright 2025 Quartile (https://www.quartile.co)

from odoo import fields, models


class MailThread(models.AbstractModel):
    _inherit = "mail.thread"

    last_chatter_update = fields.Datetime(
        string="Last Chatter Update",
        help="Datetime when a message was posted on the record.",
    )
