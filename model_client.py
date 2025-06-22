import random
import csv
import numpy as np
from tensorflow import keras

# Load the trained model and threshold
model = keras.models.load_model("ekg_autoencoder.keras")
THRESHOLD = 0.130693  # Updated threshold from reclassification

def load_random_row(filename):
    with open(filename, "r") as f:
        rows = list(csv.reader(f))
    return random.choice(rows)

def run_inference(row, label):
    x = np.array(row, dtype=np.float32).reshape(1, -1)
    recon = model.predict(x, verbose=0)
    error = float(np.mean(np.square(x - recon)))
    classification = "Anomaly" if error > THRESHOLD else "Normal"

    print(f"\n📄 {label} sample")
    print(f"🔢 Inference error: {error:.6f}")
    print(f"🔎 Classification: {classification}")

if __name__ == "__main__":
    normal_row = load_random_row("normal.csv")
    anomaly_row = load_random_row("anomaly.csv")

    run_inference(normal_row, "NORMAL")
    run_inference(anomaly_row, "ANOMALY")