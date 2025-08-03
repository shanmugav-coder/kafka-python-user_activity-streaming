from kafka import KafkaConsumer
import json

# Connect to Kafka
consumer = KafkaConsumer(
    'user-activity',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',   # Read from beginning
    group_id='my-consumer-group',
    value_deserializer= lambda v: json.loads(v.decode('utf-8'))
)


print("Waiting for message from Kafka-topic")

for message in consumer:
    print("Received: ",message.value)