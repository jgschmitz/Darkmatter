import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from pymongo import MongoClient
print 1,2,3,
# Replace the following with your MongoDB Atlas connection string
mongo_uri = "your_mongodb_atlas_connection_string"

# Connect to MongoDB Atlas
client = MongoClient(mongo_uri)

# Specify the database and collection
db = client["your_database_name"]
collection = db["your_collection_name"]

# Query MongoDB for your data (replace with your own query conditions)
query = {"organizationId": "your_organization_id", "workspaceId": "your_workspace_id"}
cursor = collection.find(query)

# Extract data for training
data = []
labels = []

for document in cursor:
    # Assuming you have features and labels in your MongoDB documents
    features = document["features"]
    label = document["label"]

    data.append(features)
    labels.append(label)

# Convert Python lists to NumPy arrays (assuming they are compatible)
import numpy as np
data = np.array(data)
labels = np.array(labels)

# Define your TensorFlow model
model = Sequential()
model.add(Dense(units=64, activation='relu', input_dim=data.shape[1]))
model.add(Dense(units=1, activation='sigmoid'))

# Compile the model (adjust the loss, optimizer, and metrics based on your task)
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
model.fit(data, labels, epochs=10, batch_size=32)

# Perform predictions or other machine learning operations as needed
