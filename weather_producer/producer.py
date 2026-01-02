import requests
import json
from kafka import KafkaProducer
from time import sleep

API_URL = "https://api.open-meteo.com/v1/forecast?latitude=48.8566&longitude=2.3522&current=temperature_2m,relative_humidity_2m,windspeed_10m"

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:
    try:
        data = requests.get(API_URL).json()
        current = data["current"]

        message = {
            "temperature": current["temperature_2m"],
            "humidity": current["relative_humidity_2m"],
            "wind": current["windspeed_10m"],
            "timestamp": current["time"]
        }

        producer.send("weather", message)
        print("Sent:", message)

    except Exception as e:
        print("Error:", e)

    sleep(60)
