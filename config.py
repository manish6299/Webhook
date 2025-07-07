from pymongo import MongoClient

# Connect to local MongoDB (or use MongoDB Atlas URI)
client = MongoClient("mongodb://localhost:27017/")
db = client["github_events"]
collection = db["events"]
