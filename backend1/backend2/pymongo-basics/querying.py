from pymongo import MongoClient
from datetime import datetime
import pprint

client = MongoClient('localhost', 27017)
db = client['aipcdb']

posts = db.timestamp
# today = datetime.date.today()
#         #gives yesterdays date
# yesterday = today - datetime.timedelta(days=1)

x=datetime.now()

#retrieve data from time

list1=[]
for post in posts.find():

   list1.append(post)
   # pprint.pprint(post)
print(list1)