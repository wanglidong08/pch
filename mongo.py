#/usr/local/bin/python3
import request
import pandas as pd
from pymongo import MongoClient
client=MongoClient()
db=client.test
my_set=db.set
my_set.insert({'name':'Tom', 'age':28})
print('helloword')