from mongoengine import *

import datetime


class LaunchRock(Document):
    email = EmailField()
    sign_date = DateTimeField(default=datetime.datetime.now)
    ip = StringField()
    http_refer = StringField()

    def __unicode__(self):
        return self.email
