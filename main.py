import webapp2
import email_helper


class Main(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Send an email to ' + email_helper.SENDER)

app = webapp2.WSGIApplication([
    ('/', Main),
], debug=True)
