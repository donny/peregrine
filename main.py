import webapp2


class Main(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('')

app = webapp2.WSGIApplication([
    ('/', Main),
], debug=True)
