# peregrine

Peregrine is a Google App Engine app that fetches Australian share prices and save them to [Google Sheets](https://www.google.com.au/sheets/about/).

### Background

This project is part of [52projects](https://donny.github.io/52projects/) and the new stuff that I learn through this project: [pygsheets](https://github.com/nithinmurali/pygsheets) and [yahoo-finance](https://github.com/lukaszbanasiak/yahoo-finance).

I read a [blog post](https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html) in February about using Google Spreadsheets as a database. I got excited since a spreadsheet also acts as an easy to use user-interface for our app. Motivated by this, I started to investigate [gspread](https://github.com/burnash/gspread) that was mentioned in the blog post. Unfortunately, it relies on the [old API](https://developers.google.com/sheets/api/v3/). Further research brought me to [pygsheets](https://pygsheets.readthedocs.io/en/latest/) that uses the current Google Sheets API (v4).

### Project

Peregrine utilises a [cron](https://cloud.google.com/appengine/docs/standard/python/config/cron) job that runs every hour from 10:00 am to 4:00 pm (the time that the Australian Stock Exchange open for trading) to fetch share prices and save them to a Google Sheets document.

The main user interface is through a spreadsheet document as shown below. This document is shared with a Google service account (`fiftytwo-peregrine`) that makes hourly edits.

![Screenshot](https://raw.githubusercontent.com/donny/peregrine/master/screenshot.png)

### Implementation

The app is implemented by one main file: [`fetch.py`](https://github.com/donny/peregrine/blob/master/fetch.py) that is invoked by a GAE cron job service every hour to retrieve share prices, process them, and save them to Google Sheets. The share prices are retrieved using a Python [library](https://github.com/lukaszbanasiak/yahoo-finance) that talks to [Yahoo! Finance](https://en.wikipedia.org/wiki/Yahoo!_Finance).

Please note that before running or deploying this application, install the dependencies using
[pip](http://pip.readthedocs.io/en/stable/):

    pip install -t lib -r requirements.txt

### Conclusion

Depending on the use cases, I think a spreadsheet is a good alternative to a database. A spreadsheet offers a familiar user interface to many people. Plus with get the benefit of mobile accessibility through Google iOS / Android apps. The [yahoo-finance](https://github.com/lukaszbanasiak/yahoo-finance) library is quite easy to use. With [pygsheets](https://pygsheets.readthedocs.io/en/latest/), sometimes I encountered memory issues on GAE instances where the process exceeded the default 128 MB memory limit. It could be because the library loads up the whole spreadsheet onto memory, but I can't be sure of the exact cause.
