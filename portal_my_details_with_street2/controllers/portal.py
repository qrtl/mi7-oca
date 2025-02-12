from odoo.addons.portal.controllers.portal import CustomerPortal

class CustomerPortalWithStreet2(CustomerPortal):
    CustomerPortal.OPTIONAL_BILLING_FIELDS.append('street2')