

# TensorFlow: EKG Anomaly Webserver and Client

## Requirements

* Python 3.10+
* Packages (install with `pip install -r requirements.txt`):

  * Flask
  * TensorFlow
  * numpy
  * pandas
  * requests
  * PySide6

---

## Setup

1. Create and activate a Python virtual environment:
   python -m venv venv
   venv\Scripts\activate       # Windows
   source venv/bin/activate    # macOS/Linux

2. Install dependencies:
   pip install -r requirements.txt

---

## How to Run

### Start the Flask Server

cd EKG\_Anomaly\_Server
venv\Scripts\activate       # or source venv/bin/activate on macOS/Linux
python serve\_ekg\_autoencoder.py

The server will run at `http://127.0.0.1:5000`.

### Run the Qt Client

cd EKG\_Client
venv\Scripts\activate
python widget.py

The GUI will open with **Submit Normal** and **Send Anom** buttons to send EKG samples to the server.

---

## Important: Configuring the Client to Connect to Your Server

By default, the client (`widget.py`) points to the server IP:

SERVER\_URL = "[http://10.0.0.xxx:5000/predict](http://10.0.0.xxx:5000/predict)"  # Change this to your server IP or localhost

* If running the server and client on the **same machine**, you can set:

  SERVER\_URL = "[http://127.0.0.1:5000/predict](http://127.0.0.1:5000/predict)"

* If the client runs on a **different machine**, set `SERVER_URL` to the **IP address of the server machine**:

  SERVER\_URL = "http\://<your-server-ip>:5000/predict"

Make sure your server firewall allows incoming connections on port `5000`.

After updating `SERVER_URL`, restart the client.

---

## Files Included

* **EKG\_Anomaly\_Server/**

  * serve\_ekg\_autoencoder.py
  * ekg\_autoencoder.keras
  * templates/index.html

* **EKG\_Client/**

  * widget.py
  * ui\_form.py
  * form.ui
  * ecg.csv

---

## Notes

* The training script is not included.
* Make sure to use compatible Python and package versions.

---
License: GPL v.2
