from pymongo import MongoClient

client = MongoClient("mongodb+srv://Sairam:Sairam12345@attendance.joaxe8j.mongodb.net/?retryWrites=true&w=majority")

db = client.Users

collection_name = db["Students"]