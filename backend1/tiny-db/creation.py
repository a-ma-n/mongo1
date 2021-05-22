from tinydb import TinyDB
from datetime import datetime


db1 = TinyDB('db1.json')
x = datetime.now()

unique_count1=0
unique_count2=0
count1=10
count2=0
count1_earlier=0
count2_earlier=0

# Week number of year, Sunday as the first day of week, 00-53

"""
put this inside the while loop
"""

if unique_count1==0:
    unique_count1=count1

db1.insert({'type': 'person','unique-count':unique_count1, 'count': count1,'time':{
           'hour':x.strftime("%H"),'weekday':x.strftime("%A"),
           'date':x.strftime("%x"),'week':x.strftime("%U"),
           'month':x.strftime("%B")}})

if unique_count2==0:
    unique_count2=count2

db1.insert({'type': 'pizza', 'unique-count':unique_count2,'count': count2,'unique-count':unique_count2,
           'time':{'Hour':x.strftime("%H"),'weekday':x.strftime("%A"),
           'date':x.strftime("%x"),'week':x.strftime("%U"),
           'month':x.strftime("%B")}})

"""
    updation of unique count
"""

if count1!=0:# whenever count is not zero and is increased
    if count1>count1_earlier:
        unique_count1=unique_count1+1
        count1_earlier=count1
else:
    unique_count1=count1

if count2 != 0:# whenever count is not zero
    if count2 > count2_earlier:
        unique_count2 = unique_count2 + 1
        count2_earlier = count2
else:
    unique_count2 = count2

'''

TODO:
----

-Merge into 1st script left
-put code in while loop in main script 
-call unique count when the total visitor number is needed

'''