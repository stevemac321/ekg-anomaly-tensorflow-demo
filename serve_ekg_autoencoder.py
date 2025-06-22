from flask import Flask, request, jsonify, render_template
import numpy as np
from tensorflow import keras
from datetime import datetime

app = Flask(__name__)
model = keras.models.load_model('ekg_autoencoder.keras')

# Updated single threshold from reclassification
THRESHOLD = 0.130693

results = []  # Store recent requests for dashboard

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    arr = np.array(data['input']).astype(np.float32)

    if arr.shape != (140,):
        return jsonify({"error": f"Input must have shape (140,), got {arr.shape}"}), 400

    arr = arr.reshape(1, -1)
    output = model.predict(arr, verbose=0)
    error = float(np.mean(np.square(arr - output)))
    anomaly = error > THRESHOLD

    result = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "output": output.flatten().tolist(),  
        "error": error,
        "anomaly": anomaly
    }
    results.append(result)

    return jsonify(result)

@app.route('/')
def index():
    return render_template('index.html', results=results[::-1])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)