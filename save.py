import pymongo
import base64
import bson
from bson.binary import Binary
from datetime import datetime

import os, subprocess

# establish a connection to the database
connection = pymongo.MongoClient(
    "mongodb+srv://andresnboza:LaVidaesBella@cluster0.doqwoff.mongodb.net/?retryWrites=true&w=majority"
)

# get a handle to the test database
db = connection.uploads
file_meta = db.file_meta
file_used = "ReadmeAppService1.md"


def main():
    print("\n ======>  Starting the save of the document  <======\n")
    coll = db.readme
    with open(file_used, "rb") as f:
        encoded = Binary(f.read())
    # coll.update({"filename": file_used}, {"filename": file_used, "file": encoded, "updatedAt": datetime.now() }, upsert = True)
    coll.aggregate({"filename": file_used, "file": encoded, "description": "test" })
    print("\n ======>  Ending the save of the document  <======\n")


main()
