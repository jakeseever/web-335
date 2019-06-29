# Title: seever-user-update.py
# Author: Jake Seever
# Date: 28 June 2019
# Description: Basic demonstration of updating documents. 

from pymongo import MongoClient
import pprint
import datetime

client = MongoClient('localhost', 27017)

db = client.web335

db.users.update_one(
    {"employee_id" : "2222222"},
    {
        "$set" : {
            "email" : "jseever@my365.bellevue.edu"
        }
    }
)

pprint.pprint(db.users.find_one({"employee_id" : "2222222"}))
