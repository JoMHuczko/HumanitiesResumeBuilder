from pymongo import MongoClient
import os

# Use an environment variable so we don't hardcode credentials
MONGO_URI = os.environ.get("MONGO_URI")

client = MongoClient(MONGO_URI)
db = client["resume_builder"]  # This is your database name
