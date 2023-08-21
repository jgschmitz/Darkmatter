#!/bin/bash
#WTF is this anyways?
# Set the MongoDB connection string
MONGO_URL="mongodb://localhost:27017"
# Run mongostat with the appropriate options
mongostat --host $MONGO_URL --discover --noheaders --json --rowcount 1
print
