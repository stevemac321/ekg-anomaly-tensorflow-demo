import csv
import random
import requests
import json

SERVER_URL = "http://10.0.0.224:5000/predict"

def load_random_row(filename):
    with open(filename, "r") as f:
        reader = list(csv.reader(f))
        return random.choice(reader)

def send_to_server(row, label):
    data = {
        "input": [float(x) for x in row]
    }
    response = requests.post(SERVER_URL, json=data)
    print(f"\n📤 Sent {label} sample")
    print(f"🔁 Server response: {response.json()}")

if __name__ == "__main__":
    normal_row = load_random_row("normal.csv")
    anomaly_row = load_random_row("anomaly.csv")

    send_to_server(normal_row, "NORMAL")
    send_to_server(anomaly_row, "ANOMALY")