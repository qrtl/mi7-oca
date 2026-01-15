#. Navigate to *Settings > Technical > Parameters > System Parameters*.
#. Set ``mail_thread_last_update.target_models`` to a comma-separated list of model names.
#. If ``mail_thread_last_update.target_models`` is empty, any chatter-enabled model will update ``last_chatter_update``.
#. Set ``mail_thread_last_update.message_types`` to a comma-separated list of message types.
#. If ``mail_thread_last_update.message_types`` is empty, any message type will update ``last_chatter_update``.
#. Example values:
   ``helpdesk.ticket,res.partner`` / ``comment,email,note``
