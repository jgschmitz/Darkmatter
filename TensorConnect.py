#load up some tastee modules 
import numpy as np
import keras
from keras import layers
from pymongo import MongoClient

# 1. Setup MongoDB Connection
MONGO_URI = "your_mongodb_atlas_connection_string"
client = MongoClient(MONGO_URI)
db = client["your_database_name"]
collection = db["your_collection_name"]

# 2. Extract data from MongoDB cleanly using projection
# Pulling only the fields we need reduces network overhead significantly
query = {"organizationId": "your_organization_id", "workspaceId": "your_workspace_id"}
projection = {"features": 1, "label": 1, "_id": 0}
cursor = collection.find(query, projection)

# Convert cursor efficiently (List comprehensions are faster than manual for-loops)
documents = list(cursor)
if not documents:
    raise ValueError("No data found matching the query criteria.")

X = np.array([doc["features"] for doc in documents])
y = np.array([doc["label"] for doc in documents])

# 3. Modern Keras Model Definition
# Keras 3 standardizes on using an explicit Input layer over input_dim/input_shape props
model = keras.Sequential([
    layers.Input(shape=(X.shape[1],)),
    layers.Dense(units=64, activation='relu'),
    layers.Dense(units=1, activation='sigmoid')
])

# 4. Compile the model 
model.compile(
    loss='binary_crossentropy', 
    optimizer='adam', 
    metrics=['accuracy']
)

# 5. Train the model
model.fit(
    X, 
    y, 
    epochs=10, 
    batch_size=32,
    validation_split=0.2 # Added a standard validation split to track overfitting
)
