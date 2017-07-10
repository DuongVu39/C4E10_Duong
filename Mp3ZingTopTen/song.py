from mongoengine import *

class Song(Document):
    artist = StringField()
    title = StringField()
    url = StringField()
