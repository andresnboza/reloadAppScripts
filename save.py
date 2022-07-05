#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import the datetime and time library
import datetime
import time

import base64
import json
import bson
from bson.binary import Binary

# import the MongoClient class of the PyMongo library
from pymongo import MongoClient

# import ObjectID from MongoDB's BSON library
# (use pip3 to install bson)
from bson import ObjectId

import certifi
import sys

print(sys.argv)

file_used = sys.argv[1]
MONGO_URI = sys.argv[2]

print("file_used", file_used)
print("MONGO_URI", MONGO_URI)

# create a client instance of the MongoClient class
# mongo_client = MongoClient('mongodb+srv://andresnboza:LaVidaesBella@cluster0.doqwoff.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=certifi.where())
mongo_client = MongoClient(MONGO_URI, tlsCAFile=certifi.where())

# create database and collection instances
db = mongo_client["uploads"]
col = db["readme"]

"""
REPLACING ALL OF A MONGODB DOCUMENT'S DATA
USING PYMONGO'S replace_one() METHOD
"""
# create filter query to replace a document
# file_used = "ReadmeAppService1.md"
query = {"file_name": file_used}

# Python program to convert text
# file to JSON

# dictionary where the lines from
# text will be stored
dict1 = {}

# creating dictionary
with open(file_used) as fh:
    for line in fh:

        # reads each line and trims of extra the spaces
        # and gives only the valid words
        command, description = line.strip().split(None, 1)

        dict1[command] = description.strip()

# add "date" and "number" key-value pairs to the data
replacement_data = {
    "createdAt": datetime.datetime.now(),
    "file_name": file_used,
    "encoded": dict1
}


# pass dict objects to PyMongo's replace_one() method
result = col.replace_one(query, replacement_data, upsert=True)

# print ("raw:", result.raw_result)
print("acknowledged:", result.acknowledged)
# print ("matched_count:", result.matched_count)

mongo_client.close()
