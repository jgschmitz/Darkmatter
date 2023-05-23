name=mapr-to-s3-pipeline
connector.class=com.mapr.kafka.connect.file.MapRSourceConnector
tasks.max=1
mapr.source.path=/path/to/mapr/file
topic=my-topic
