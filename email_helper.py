SENDER = 'info@fiftytwo-cardinal.appspotmail.com'

HELP_MESSAGE = """Dear user,

Send an email to {} with any of the following subject line:

"help" to get the list of valid email commands.
"subscribe" followed by space-delimited keywords to subscribe to.
"unsubscribe" followed by space-delimited keywords to unsubscribe to.
"list" to get the list of subscribed keywords.
"remove" to cancel the email notifications.

Thanks
""".format(SENDER)

LIST_MESSAGE = """Dear user,

You have subscribed to the following keywords:

{}

Thanks
"""

REMOVE_MESSAGE = """Dear user,

You have been removed from this service.

Thanks
"""

NEW_DEALS_MESSAGE = """Dear user,

You have new deals:

{}

Thanks
"""
