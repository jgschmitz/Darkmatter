const { KafkaClient, Consumer } = require('kafka-node');
const { MongoClient } = require('mongodb');

const kafkaHost = 'localhost:9092';
const topic = 'sql-data';
const mongodbUri = 'mongodb://localhost:27017/';
const dbName = 'sql-to-mongodb';

let mongoClient;

// Connect to MongoDB with async/await
async function connectToMongoDB() {
  try {
    mongoClient = await MongoClient.connect(mongodbUri, { useUnifiedTopology: true });
    console.log('Connected to MongoDB');
    return mongoClient.db(dbName);
  } catch (err) {
    console.error(`Failed to connect to MongoDB: ${err}`);
    process.exit(1);
  }
}

// Kafka Consumer setup
const consumer = new Consumer(
  new KafkaClient({ kafkaHost }),
  [{ topic }],
  { autoCommit: true }
);

// Listen for incoming Kafka messages and insert into MongoDB
async function startKafkaConsumer() {
  const db = await connectToMongoDB();

  consumer.on('message', async message => {
    console.log(`Received message: ${message.value}`);
    try {
      // Ensure message is valid JSON
      const data = JSON.parse(message.value);

      // Insert the message into MongoDB
      await db.collection(topic).insertOne({ data });
      console.log('Message successfully inserted into MongoDB');
    } catch (error) {
      console.error(`Failed to insert message into MongoDB: ${error.message}`);
    }
  });

  consumer.on('error', error => {
    console.error(`Kafka consumer error: ${error.message}`);
  });

  // Graceful shutdown
  process.on('SIGINT', async () => {
    console.log('Shutting down...');
    consumer.close(true, () => {
      console.log('Kafka consumer closed.');
    });
    await mongoClient.close();
    console.log('MongoDB connection closed.');
    process.exit(0);
  });
}

// Start the Kafka consumer
startKafkaConsumer();
