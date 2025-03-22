import pymongo
# 2.0 clean
# MongoDB connection details
CONNECTION_STRING = "mongodb+srv://<username>:<password>@cluster.mongodb.net/test"
DATABASE_NAME = "your_database_name"
COLLECTION_NAME = "your_collection_name"

# Sample data to insert
data_to_insert = {
    "name": "John Doe",
    "age": 30,
    "email": "johndoe@example.com"
}

# Connect to MongoDB, insert data, and close automatically
with pymongo.MongoClient(CONNECTION_STRING) as client:
    collection = client[DATABASE_NAME][COLLECTION_NAME]
    inserted_data = collection.insert_one(data_to_insert)
    print(f"Data inserted with ID: {inserted_data.inserted_id}")
