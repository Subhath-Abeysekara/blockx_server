import time
from pymongo import MongoClient
import os
import env


def connect_client():
    CONNECTION_STRING = env.MONGO_URL
    while True:
        try:
            client = MongoClient(CONNECTION_STRING)
            return client
        except Exception as e:
            print(f"Error connecting to database: {e}")
            print("Retrying in 5 seconds...")
            time.sleep(5)

client = connect_client()

def connect_mongo_user():
    db_Name = client['blocx']
    collection_name = db_Name["user"]
    return collection_name

def connect_mongo_post():
    db_Name = client['blocx']
    collection_name = db_Name["posts"]
    return collection_name

def connect_mongo_requests():
    db_Name = client['blocx']
    collection_name = db_Name["requests"]
    return collection_name

# collection_name = connect_mongo_user()
# # data = {
# #     "name":"subhath"
# # }
# # collection_name.insert_one(data)
# data = collection_name.find()
# for user in data:
#     print(user)
# # print(data)