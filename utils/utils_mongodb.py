import pymongo
from pymongo import MongoClient


# Instatiate MongoDB Client
mongo_user = 'jobi-service-user'
mongo_pass = 'mnsDkMSWbGFK2FPd'
mongo_conn_string = f'mongodb+srv://{mongo_user}:{mongo_pass}@jobi-cluster.bc1kiqp.mongodb.net/?retryWrites=true&w=majority'

cluster = MongoClient(mongo_conn_string)
db = cluster["test"]
collection = db["test"]


# Insert a single document into Collection
post = {"_id": 0, "name": "tim", "score": 5}
collection.insert_one(post)


# Insert multiples documents into Collection
post1 = {"_id": 1, "name": "joe"}
post2 = {"_id": 2, "name": "bill"}

collection.insert_many([post1, post2])


# Query documents into Collection
results = collection.find({"name": "bill"})
print(results)

for result in results:
    print(result["_id"])


# Query one document
results = collection.find_one({"_id": 0})
print(results)


# Query all document
results = collection.find({})

for x in results:
    print(x)


# Delete one document
results = collection.delete_one({"_id": 0})


# Delete many document
results = collection.delete_many({})


# Update one document
results = collection.update_one({"_id": 1}, {"$set": {"name": "tim"}})


# Update many documents
results = collection.update_many({"_id": 1}, {"$inc": {"hello": 5}})


# Count Documents
doc_count = collection.count_documents({})
print(doc_count)
