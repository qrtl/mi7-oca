1. Go to Settings > General Settings.  
2. Search for "Mail Domain Blacklist" and enter the domains you want to blacklist, separated  
   by commas.  

Server configuration
~~~~~~~~~~~~~~~~~~~~~

In the odoo.conf file, set db_list = True to allow listing all databases.
In this case, blacklist domains from all databases will affect every database.
Set db_list = False and explicitly define db_name if you want to load only
the target database. In this case, blacklist domains will affect only that
database.

Note: Every time you update the "Mail Domain Blacklist," you need to restart the Odoo server
for the change to take effect.
