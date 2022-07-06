#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
from bson.binary import Binary
from pymongo import MongoClient
from bson import ObjectId
import certifi
import sys

file_used = sys.argv[1]
MONGO_URI = sys.argv[2]

mongo_client = MongoClient(MONGO_URI + '', tlsCAFile=certifi.where())

db = mongo_client["uploads"]
col = db["readmes"]

print("######" + file_used + "######")

key = {"file_name": file_used}
dict = {}
num = 0

# creating dictionary
with open(file_used) as fh:
    for line in fh:
        description = line.strip()
        dict[str(num)] = description.strip()
        num += 1

# add "date" and "number" key-value pairs to the data
data = {
    "createdAt": datetime.datetime.now(),
    "file_name": file_used,
    "encoded": dict
}

col.update(key, data, upsert=True)
mongo_client.close()
