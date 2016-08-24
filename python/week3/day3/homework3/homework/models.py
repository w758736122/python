from django.db import models
from mongoengine import *
from mongoengine import connect
connect('week_two_bigHW',host='127.0.0.1',port=27017)

class ArtiInfo(Document):
    trading_site = StringField()
    title = StringField()
    price=StringField()
    time = StringField()
    url = StringField()
    type = ListField(StringField())
    new_old=StringField()
    meta={
        'collection':'week_two_bigHW_sheet2'
    }

