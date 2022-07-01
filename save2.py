#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# import the datetime and time library
import datetime, time

import base64
import bson
from bson.binary import Binary

# import the MongoClient class of the PyMongo library
from pymongo import MongoClient

# import ObjectID from MongoDB's BSON library
# (use pip3 to install bson)
from bson import ObjectId

import certifi

# create a client instance of the MongoClient class
mongo_client = MongoClient('mongodb+srv://andresnboza:LaVidaesBella@cluster0.doqwoff.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=certifi.where())

# create database and collection instances
db = mongo_client["uploads"]
col = db["readme"]

"""
REPLACING ALL OF A MONGODB DOCUMENT'S DATA
USING PYMONGO'S replace_one() METHOD
"""
# create filter query to replace a document
file_used = "ReadmeAppService1.md"
query = {"file_name" : file_used }

with open(file_used, "rb") as f:
    encoded = Binary(f.read())

# add "date" and "number" key-value pairs to the data
replacement_data = {
    "createdAt" : datetime.datetime.now(),
    "file_name" : file_used,
    "encoded": encoded
}


# pass dict objects to PyMongo's replace_one() method
result = col.replace_one( query, replacement_data, upsert=True )

# print ("raw:", result.raw_result)
print ("acknowledged:", result.acknowledged)
# print ("matched_count:", result.matched_count)

mongo_client.close()