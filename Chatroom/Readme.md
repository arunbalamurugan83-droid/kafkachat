# Kafka Chatroom

A simple real-time chat system built with **Apache Kafka** and **Python**. This allows multiple users to send and receive messages via a Kafka topic. Each user runs a separate Python client and can chat in real time.

---

## **Features**

- Two-way chat between users.
- Real-time messaging using Kafka producer and consumer.
- Unique Kafka consumer group per user to avoid reading your own messages.
- Multi-threaded consumer to listen for messages in the background.
- Upcoming feature multi user supports more than 3

---

## **Prerequisites**

- Python 3.x
- Kafka 3.x or above installed locally
- Kafka Python client: `kafka-python` library

Install dependencies:

```bash
pip install kafka-python
