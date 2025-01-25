from pymongo import MongoClient
from bson.objectid import ObjectId

class MongoRepository:
    def __init__(self, collection_name):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['advisor_matching']
        self.collection = self.db[collection_name]
    
    def insert(self, data):
        result = self.collection.insert_one(data)
        return str(result.inserted_id)

    def find_by_id(self, object_id):
        return self.collection.find_one({"_id": ObjectId(object_id)})

    def find(self, query):
        return list(self.collection.find(query))

    def update(self, object_id, data):
        self.collection.update_one({"_id": ObjectId(object_id)}, {"$set": data})
