from google.appengine.ext import ndb

class Deal(ndb.Model):
    link = ndb.StringProperty() # This serves as the key.
    title = ndb.StringProperty()
    description = ndb.TextProperty()
    keywords = ndb.StringProperty(repeated=True)
    new = ndb.BooleanProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)

class Person(ndb.Model):
    email = ndb.StringProperty() # This serves as the key.
    keywords = ndb.StringProperty(repeated=True)
