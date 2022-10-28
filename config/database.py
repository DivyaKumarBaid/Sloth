# mongoDB driver
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

# connection between mongodb and database.py
client = MongoClient(os.getenv('MONGOURL'))

database = client.code

user_col = database.users

posts = database.posts

code = database.code

unverified_user = database.unverified
