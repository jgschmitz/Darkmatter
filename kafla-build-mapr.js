{
  "name": "maprfs-source",
  "config": {
    "connector.class": "io.confluent.connect.mapr.fs.MapRfsSourceConnector",
    "tasks.max": "1",
    "maprfs.source.path": "/path/to/maprfs",
    "key.converter": "org.apache.kafka.connect.storage.StringConverter",
    "value.converter": "org.apache.kafka.connect.json.JsonConverter",
    "value.converter.schemas.enable": "false",
    "topics": "maprfs-topic"
  }
}

{
  "name": "s3-sink",
  "config": {
    "connector.class": "io.confluent.connect.s3.S3SinkConnector",
    "tasks.max": "1",
    "topics": "maprfs-topic",
    "s3.bucket.name": "your-s3-bucket",
    "key.converter": "org.apache.kafka.connect.storage.StringConverter",
    "value.converter": "org.apache.kafka.connect.json.JsonConverter",
    "value.converter.schemas.enable": "false"
  }
}
