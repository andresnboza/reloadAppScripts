import pymongo
import base64
import bson
from bson.binary import Binary
from datetime import datetime

import os, subprocess
import sys

file_used = sys.argv[1]
MONGO_URI = sys.argv[2]

print("file_used", file_used)
print("MONGO_URI", MONGO_URI)

# establish a connection to the database
connection = pymongo.MongoClient(MONGO_URI)

# get a handle to the test database
db = connection.uploads
file_meta = db.file_meta

def main():
    print("\n ======>  Starting the save of the document  <======\n")
    coll = db.readme
    with open(file_used, "rb") as f:
        encoded = Binary(f.read())
    # coll.update({"filename": file_used}, {"filename": file_used, "file": encoded, "updatedAt": datetime.now() }, upsert = True)
    coll.aggregate({"filename": file_used, "file": encoded, "description": "test" })
    print("\n ======>  Ending the save of the document  <======\n")


main()
