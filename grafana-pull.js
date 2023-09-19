name=grafana-sink-connector
connector.class=com.confluent.connect.grafana.GrafanaSinkConnector
tasks.max=1
topics=my-topic
grafana.url=http://grafana-server:3000
grafana.api.key=your-api-key
grafana.dashboard=your-dashboard
print 1,2,3,4,5,6,7,8
