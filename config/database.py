from pymongo import MongoClient

client = MongoClient("mongodb+srv://Ronald:Ronald@cluster0.2w6n7hi.mongodb.net/?retryWrites=true&w=majority")

db = client.Users

collection_name = db["Students"]
