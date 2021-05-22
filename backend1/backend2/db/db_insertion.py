from pymongo import MongoClient
from datetime import datetime
import time
import pprint

client = MongoClient('localhost', 27017)
db = client['aipcdb']

unique_count1=15
unique_count2=15
count1=10
count2=0
count1_earlier=0
count2_earlier=0
x=datetime.now()
"""
pizza
-merge in the for loop for inserting in the db
"""
# for i in range(1):#
#     post={'type': 'pizza','unique-count':unique_count1, 'count': count1,'time':{
#                'hour':x.strftime("%H"),'weekday':x.strftime("%A"),
#                'date':x.strftime("%x"),'week':x.strftime("%U"),
#                'month':x.strftime("%B"),"year":x.strftime("%G"),"month":x.strftime("%H"),
#                                          "week": x.strftime("%H"),'weekday':x.strftime("%H"),'daynumber':x.strftime("%j")}}
#     posts = db.timestamp
#     post=posts.insert_one(post)
#     # we can vary gap between timestamps here
#     time.sleep(1)
#     count1=count1+1
#     # print(post)
"""
person
-merge in the for loop for inserting in the db
"""
count_new=0

for i in range(1):
    posts = db.timestamp
    list1 = []
    post0=[{'type': 'person','unique-count':0, 'count': 12,
               'hour':(int)(x.strftime("%H")),'weekday':(int)(x.strftime("%A")),
               'date':x.strftime("%x"),'week':(int)(x.strftime("%U")),
               'month':x.strftime("%B")}]
    c=0
    """
    look how to query to get the docs acc to date
    fetching the date from the db and matching with the date
    """
    # for post in posts.find():
    #     if post['value']['date']==x.strftime("%x"):
    #         # print(post['value']['date'])
    #         # print("iou")
    #         if post['value']['hour']==17:
    #             print(post['value']['count'])

    """
    adding data to the same document
    """
    # Narrow down to the today's date doc

    for post in posts.find():
        if post['value']['date']==x.strftime("%x"):
            """
            To-do:
            1-fetch data
            2-append data
            3-upload data
            """
            print('post is',post,'\n')
            list1.append(post)

    print('list is',list1,'\n')
    list1.append({'value':post0})
    print(list1)

    """
    check if the collection exists else create a new one
    """
    # if posts!=0:
    # post1=posts.
    # print(list1)
    # for i in list1:
        #post1=posts.insert_many(i)
        # we can vary gap between timestamps here
        # time.sleep(1)
    # count1=count1+1
    # else:
    posts.insert_one(list1)
    """
    TODO:
    -create a list 
    -store all groups in a list
    -mark the document by a date
    
    add data to the same docs
    fetch data into the hour db
    """
