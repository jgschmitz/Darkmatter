#!/bin/bash
#WTF is this anyways?
# Set the MongoDB connection string
MONGO_URL="mongodb://localhost:27017"
print 1,2,3
# Run mongostat with the appropriate options
mongostat --host $MONGO_URL --discover --noheaders --json --rowcount 1
