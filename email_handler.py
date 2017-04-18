import logging
import webapp2
import re
from google.appengine.ext.webapp.mail_handlers import InboundMailHandler
from google.appengine.api import mail
import email_helper


class EmailHandler(InboundMailHandler):

    def receive(self, mail_message):
        logging.info("RECV: " + mail_message.sender +
                     " : " + mail_message.subject)

        message = mail.EmailMessage(subject='Info',
                                    sender=email_helper.SENDER)
        message.to = mail_message.sender

        subject = mail_message.subject.lower()
        sender = mail_message.sender

        # keywords = person.keywords
        # Get the data from the Spreadsheet
        message.body = email_helper.LIST_MESSAGE.format(
            ' '.join(keywords))

        message.send()


app = webapp2.WSGIApplication([
    EmailHandler.mapping()
], debug=True)
