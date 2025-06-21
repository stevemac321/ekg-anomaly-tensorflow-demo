

# TensorFlow: EKG Anomaly Webserver and Client
##Overview from TensorFlow: https://www.tensorflow.org/tutorials/generative/autoencoder
## Requirements

* Python 3.10+
* Packages (install with `pip install -r requirements.txt`):

  * Flask
  * TensorFlow
  * numpy
  * pandas
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
python serve_ekg_autoencoder.py

The server will run at `http://127.0.0.1:5000`.
Run the test.py in the client directory to get a sample out of the .csv files.

You can view the prediction results and logs on this web page in your browser. "EKG Predictions Dashboard".  
Example:

2025-06-18 05:13:10
Prediction: [0.09907367825508118, -0.042691461741924286, 0.5079333186149597, 0.1889864206314087, 0.5483210682868958 ...]
Error: 0.5520787835121155
Anomaly: False

---
License: GPL v.2
