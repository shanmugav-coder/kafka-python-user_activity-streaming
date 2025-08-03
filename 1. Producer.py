from kafka import KafkaProducer #KafkaProducer from kafka-python to connect to Kafka.
import json #json to convert Python dicts into JSON strings.
import time #time to add timestamps and delay messages
import random #random to simulate random user behavior.

# Simulated user actions
actions = ['login', 'logout', 'search', 'click', 'purchase']

# Connect to Kafka
producer = KafkaProducer(
    bootstrap_servers='localhost:9092', # connect to your locally running Kafka broker.
    value_serializer=lambda v: json.dumps(v).encode('utf-8') 
#value_serializer: transforms Python dictionaries (dict) into JSON strings, and then encodes them as UTF-8 (since Kafka only sends bytes).
)

# Send events forever
while True:
    event = {
        'user_id': random.randint(1, 1000),
        'action': random.choice(actions),
        'timestamp': time.time()
    }

    # Send message to Kafka
    producer.send('user-activity', value=event)
    print("Sent:", event)
    time.sleep(1)
