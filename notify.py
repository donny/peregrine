import logging
import webapp2
from model import Deal, Person
from google.appengine.api import mail
import email_helper


class Notify(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'

        people = Person.query().fetch()
        new_deals = Deal.query(Deal.new == True).fetch()

        new_emails = {}

        for person in people:
            for new_deal in new_deals:
                intersect = set(new_deal.keywords) & set(person.keywords)
                if len(intersect) != 0:
                    if person.email not in new_emails:
                        new_emails[person.email] = []
                    new_emails[person.email].append(new_deal)

        for new_deal in new_deals:
            new_deal.new = False
            new_deal.put()

        for email, deals in new_emails.iteritems():
            deals_text = ''
            for deal in deals:
                deals_text += deal.link + ' : ' + deal.title + '\n'
            message = mail.EmailMessage(subject='New Deals',
                                        sender=email_helper.SENDER)
            message.to = email
            message.body = email_helper.NEW_DEALS_MESSAGE.format(
                deals_text)
            message.send()
            logging.info("Email with " + str(len(deals)) +
                         " new deals sent to " + email)

        self.response.write('OK')

app = webapp2.WSGIApplication([
    ('/notify', Notify),
], debug=True)
