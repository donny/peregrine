import logging
import webapp2
import re
from bs4 import BeautifulSoup
from google.appengine.api import urlfetch
from model import Deal

FEED_URL = 'https://www.ozbargain.com.au/deals/feed'


class Fetch(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'

        try:
            result = urlfetch.fetch(FEED_URL, validate_certificate=True)
            if result.status_code == 200:
                soup = BeautifulSoup(result.content, 'xml')
                items = soup.findAll('item')
                for item in items:
                    link = item.link.text.encode('utf-8')
                    title = item.title.text.encode('utf-8')
                    description = item.description.text.encode('utf-8')

                    deal = Deal.get_by_id(link)
                    if deal == None:
                        deal = Deal(id=link, link=link, title=title,
                                    description=description, new=True)
                        keywords = re.sub(r'\W+', ' ', title)
                        keywords = keywords.lower().split(' ')
                        # To remove empty strings.
                        keywords = filter(None, keywords)
                        keywords = list(set(keywords))  # To remove duplicates.
                        deal.keywords = keywords
                        deal.put()

                self.response.write('OK')
            else:
                self.response.write('ERROR')
        except urlfetch.Error:
            logging.exception('Caught exception fetching data')
            self.response.write('EXCEPTION')

app = webapp2.WSGIApplication([
    ('/fetch', Fetch),
], debug=True)
