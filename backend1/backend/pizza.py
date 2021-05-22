
import datetime
import mongoengine


class Pizza(mongoengine.Document):
    registered_date = mongoengine.DateTimeField(default=datetime.datetime.now)
    length = mongoengine.FloatField(required=True)

    meta = {
        'db_alias': 'core',
        'collection': 'db1'
    }