from pymongo import MongoClient
import os

# Use env variable from Render or fall back to localhost
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(MONGO_URI)
db = client["cnc_ai"]

def get_mongo_collection(name: str):
    return db[name]
