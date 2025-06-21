import pandas as pd
import requests
import json

# Load comma-delimited files: 140 floats per row, no label column
regular_df = pd.read_csv("regular.csv", header=None)
anomaly_df = pd.read_csv("anomaly.csv", header=None)

# Pick one row from each
normal_sample = regular_df.iloc[0].tolist()
anomaly_sample = anomaly_df.iloc[0].tolist()

def send_sample(sample, label):
    payload = {"input": sample}
    try:
        response = requests.post(
            "http://10.0.0.224:5000/predict",
            headers={"Content-Type": "application/json"},
            data=json.dumps(payload)
        )
        print(f"\n🧪 Sent label {label}")
        print("Status Code:", response.status_code)
        print("Response JSON:", response.json())
    except Exception as e:
        print(f"❌ Error sending label {label}:", e)

# Send both
send_sample(normal_sample, label="regular")
send_sample(anomaly_sample, label="anomaly")