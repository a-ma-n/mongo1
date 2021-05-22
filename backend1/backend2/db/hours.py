from pymongo import MongoClient
from datetime import datetime
import time
from db_insertion import *

'''
mogodb details
'''

client = MongoClient('localhost', 27017)
db = client['aipcdb']


x= datetime.now()

'''
line denotes start of an hour 
-we take the difference b/w the unique times at 2 different intervals 
'''
if x.strftime("%M")==0: # store the hourly counts after every hour,

    """
    fetch 2 variables 
    -1:stores the older count 
    -2:stores the newer count
    
    considering for 1 day add condition for the day switch
    """
    hr = x.strftime("%H")
    dt = x.strftime("%x")
    if hr!=0:
        q1 = db.timestamp.time.find_one({"date": dt, "hour": hr - 1})
        q2 = db.timestamp.time.find_one({"date": dt, "hour": hr})
    elif x.strftime("%j"):# not the start of the year

        q1 = db.timestamp.time.find_one({"daynumber":x.strftime("%j")-1, "hour": 23})
        q2 = db.timestamp.time.find_one({"daynumber":x.strftime("%j"), "hour": hr})

    else: # year started & previous year was not a leap year
        """
        dt: stores date of previous year
        y:stores the value of last year
        """
        dt=365
        y=x.strftime("%G")
        if y%400==0 or (y%4 and y%100!=0) :
            dt=366
        q1 = db.timestamp.time.find_one({"year":ly-1,"daynumber": dt, "hour": 24})
        q2 = db.timestamp.time.find_one({"date": dt, "hour": hr})

    # fetch the doc of prev hour
    uc1 =q1['unique-count']
    # fetch the doc of current hour
    uc2=q2['unique-count']






    tc=person[0]['count']

    #query between 2 limits and return
    # t1=person
    # while :
    # if tc==0:
    #     zv1=zv1+1
    # stores the hour of the day along with the zero visit hours(till date)
    db2.insert({'column':'hours','visits-in-the-hour':tc,'zero-visit-hours': zv1,'time':{'Hour':qr.strftime("%H"),'weekday':qr.strftime("%A"),
           'date':qr.strftime("%x"),'week':qr.strftime("%U"),
           'month':qr.strftime("%B")}})
