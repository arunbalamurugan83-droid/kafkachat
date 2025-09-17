from kafka import KafkaProducer, KafkaConsumer
import threading
import json

# --------- CONFIGURATION ---------
TOPIC = "chat-room"
BOOTSTRAP_SERVERS = ['localhost:9092']
USER = input("Enter your username: ")  # Ask for UserA / UserB
# ---------------------------------

# Producer
producer = KafkaProducer(
    bootstrap_servers=BOOTSTRAP_SERVERS,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Consumer
consumer = KafkaConsumer(
    TOPIC,
    bootstrap_servers=BOOTSTRAP_SERVERS,
    auto_offset_reset='earliest',   # Read from beginning
    enable_auto_commit=True,
    group_id=f"{USER}_group",       # unique group per user
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

# Listen for incoming messages
def listen():
    for message in consumer:
        msg = message.value
        if msg["user"] != USER:
            # Print message, then reprint the prompt without extra newline
            print(f"\r{msg['user']}: {msg['text']}\nYou: ", end="", flush=True)


# Run consumer in background
threading.Thread(target=listen, daemon=True).start()

# Producer loop
print(f"Welcome {USER}! Start chatting (type 'exit' to quit):")
while True:
    text = input("You: ")
    if text.lower() == "exit":
        break
    producer.send(TOPIC, {"user": USER, "text": text})
    producer.flush()


    
