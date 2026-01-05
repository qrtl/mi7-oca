This module allows adding domains to the mail domain blacklist to prevent Odoo from assuming  
that users with the same domain belong to the same organization.

The effect of blacklist domains depends on how the Odoo server is configured to
load databases. In environments where multiple databases can be listed and
accessed, blacklist entries apply across all of them. When the server loads only
a single, explicit database, the blacklist affects only that database.
