import logging
import webapp2
from model import Deal, Person
from google.appengine.api import mail
import email_helper
from google.appengine.ext import ndb


class Clean(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'

        old_deals = Deal.query(Deal.new == False)
        ndb.delete_multi([d.key for d in old_deals])

        self.response.write('OK')

app = webapp2.WSGIApplication([
    ('/clean', Clean),
], debug=True)
