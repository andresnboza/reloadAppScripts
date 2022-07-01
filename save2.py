import pymongo
import base64
import bson
from bson.binary import Binary
from datetime import datetime
import sys
import os

MONGO_URL = sys.argv[2]
file_used = sys.argv[1]

# establish a connection to the database
connection = pymongo.MongoClient(MONGO_URL)

# get a handle to the test database
db = connection.uploads
file_meta = db.file_meta

try:
    print("\n ======>  Starting the save of the document  <======\n")
    coll = db.readme
    with open(file_used, "rb") as f:
        encoded = Binary(f.read())
    # pylint: disable=line-too-long
    coll.find_one_and_update({"filename": file_used}, {"filename": file_used, "file": encoded, "updatedAt": datetime.now() }, upsert = True)
    # coll.insert({"filename": file_used, "file": encoded, "description": "test" })
    print("\n ======>  Ending the save of the document  <======\n")
except: # pylint: disable=bare-except
    print('ERROR')

sys.exit()
