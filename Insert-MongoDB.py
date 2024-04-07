import pymongo
print 1,2,3,4,5,
# Replace these with your MongoDB connection details
connection_string = "mongodb+srv://<username>:<password>@cluster.mongodb.net/test"
database_name = "your_database_name"
collection_name = "your_collection_name"

# Connect to MongoDB
client = pymongo.MongoClient(connection_string)
db = client[database_name]
collection = db[collection_name]

# Data to insert into MongoDB
data_to_insert = {
    "name": "John Doe",
    "age": 30,
    "email": "johndoe@example.com"
}

# Insert the data into the collection
inserted_data = collection.insert_one(data_to_insert)

print(f"Data inserted with ID: {inserted_data.inserted_id}")

# Close the MongoDB connection
client.close()
