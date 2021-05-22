from tinydb import TinyDB, Query
from creation import unique_count1

db1 = TinyDB('db1.json')

User = Query()
person=db1.search(User.type == 'person')

# represents the hour

print(person[0]['time']['hour'])
print('count is ',unique_count1)