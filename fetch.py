import logging
import webapp2
import re
from google.appengine.api import urlfetch
from model import Deal
from yahoo_finance import Share
import pygsheets

SERVICE_CREDS = 'service_creds.json'
SHEET_FILE_NAME = 'Share Price Data'
SHEET_WORK_NAME = 'Data'


class Fetch(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'

        gs = pygsheets.authorize(service_file=SERVICE_CREDS, no_cache=True)
        sh = gs.open(SHEET_FILE_NAME)
        ws = sh.worksheet_by_title(SHEET_WORK_NAME)

        try:
            shares = ['^AORD', 'FXJ.AX']
            for symbol in shares:
                share = Share(symbol)
                s_price = share.get_price()
                s_name = share.get_name()
                symbol_cells = sh.find(symbol)
                if len(symbol_cells) == 0:
                    ws.append_table(values=[s_name, symbol, s_price])
                else:
                    symbol_cell = symbol_cells[0]
                    symbol_cell.neighbour('left').value = s_name
                    symbol_cell.neighbour('right').value = s_price

            self.response.write('OK')
        except:
            logging.exception('Caught exception in fetch')
            self.response.write('EXCEPTION')

app = webapp2.WSGIApplication([
    ('/fetch', Fetch),
], debug=True)
