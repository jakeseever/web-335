# Title: seever-user-service.py
# Author: Jake Seever
# Date: 27 June 2019
# Description: Basic demonstration of querying and creating documents.

from pymongo import MongoClient
import pprint
import datetime

client = MongoClient('localhost', 27017)

db = client.web335

user = {
    "first_name" : "Ryan",
    "last_name" : "Wojicechowski",
    "employee_id" : "2222222",
    "email" : "wojo1@gmail.com",
    "date_created" : datetime.datetime.utcnow()
    
}

user_id = db.users.insert_one(user).inserted_id
print(user_id)

pprint.pprint(db.users.find_one({"employee_id" : "2222222"}))
