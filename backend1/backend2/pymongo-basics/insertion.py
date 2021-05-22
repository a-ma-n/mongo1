from pymongo import MongoClient
from datetime import datetime
import time

client = MongoClient('localhost', 27017)

db = client['aipcdb']
new_count=0
unique_count1=count1=0

x=datetime.now()
for i in range(1):
    post={'type':'person','unique-count':unique_count1, 'count': count1,
               'hour':(int)(x.strftime("%H")),'weekday':x.strftime("%A"),
               'date':x.strftime("%x"),'week':(int)(x.strftime("%U")),
               'month':x.strftime("%B")}
    posts = db.timestamp
    # new_count=new_count+1
    number=str(new_count)
    post_id=posts.insert_one({'value':[post]})
    # we can vary gap between timestamps here
    # time.sleep(1)
    count1=count1+1
    print(post_id)
"""
when date changes
1)reset new_count (update new count when adding more to the same doc)
2)shift to a new document
"""