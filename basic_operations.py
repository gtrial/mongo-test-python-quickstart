import os
import certifi
import pymongo
from dotenv import load_dotenv
from pymongo import MongoClient

# Load MongoDB connection string from .env file
load_dotenv()
uri = os.environ['MONGODB_URI']

# Establish MongoDB connection with error handling
try:
    with MongoClient(uri, tlsCAFile=certifi.where()) as client:
        print("Connected to MongoDB cluster!")
        for database_name in client.list_database_names():
            print(database_name)
except pymongo.errors.ConnectionFailure as e:
    print(f"Could not connect to MongoDB: {e}")
