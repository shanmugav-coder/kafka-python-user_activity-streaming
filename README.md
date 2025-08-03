# Real-Time User Activity Streaming with Kafka and Python

This project demonstrates a basic streaming pipeline where simulated user activity is sent to a Kafka topic using a Python producer and read using a Python consumer.

## Tech Stack
- Apache Kafka 3.9.1
- Python 3.x
- kafka-python
- Zookeeper

## Setup Instructions

### Prerequisites
- Java (OpenJDK 17+)
- Kafka & Zookeeper installed locally
- Python 3.x installed

### Kafka Setup
1. Start Zookeeper:
```bash
.\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties
````

2. Start Kafka Broker:

```bash
.\bin\windows\kafka-server-start.bat .\config\server.properties
```

3. Create Kafka Topic:

```bash
.\bin\windows\kafka-topics.bat --create --topic user-activity --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
```

4. Verify Topic:

```bash
.\bin\windows\kafka-topics.bat --list --bootstrap-server localhost:9092
```

### Python Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

### Running the App

* Run Producer:

```bash
python producer.py
```

* Run Consumer:

```bash
python consumer.py
```

## Output Example

```json
{"user_id": 57, "action": "login", "timestamp": 1722624775.127}
```

## Concepts Covered

* Kafka topic creation
* Python Kafka producer/consumer
* JSON serialization/deserialization
* Real-time data streaming pipeline

## Future Enhancements

* Persist data to database (PostgreSQL, MongoDB)
* Stream processing frameworks (Spark/Flink)
* Deploy to cloud (AWS MSK, Confluent Cloud)

 **Create `requirements.txt`**

Create a file named `requirements.txt` with:

```

kafka-python==2.0.2

```
