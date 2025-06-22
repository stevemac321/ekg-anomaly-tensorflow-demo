import numpy as np
import csv
from tensorflow import keras

# Load model and threshold
model = keras.models.load_model("ekg_autoencoder.keras")
THRESHOLD = 0.130693  # Final inference threshold

def check_file(filename, direction):
    violations = 0
    total = 0
    with open(filename, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            total += 1
            arr = np.array(row, dtype=np.float32).reshape(1, -1)
            recon = model.predict(arr, verbose=0)
            error = float(np.mean(np.square(arr - recon)))

            if (direction == "normal" and error > THRESHOLD) or \
               (direction == "anomaly" and error < THRESHOLD):
                violations += 1
                print(f"{direction.upper()} FAIL | Error: {error:.6f} | Row: {row}")
    return violations, total

# Run checks
print("🔍 Checking normal.csv for false positives...")
normal_violations, normal_total = check_file("normal.csv", "normal")

print("\n🔍 Checking anomaly.csv for false negatives...")
anomaly_violations, anomaly_total = check_file("anomaly.csv", "anomaly")

# Summary
print("\n📊 Summary:")
print(f"Normal.csv — {normal_violations} violations out of {normal_total} rows")
print(f"Anomaly.csv — {anomaly_violations} violations out of {anomaly_total} rows")