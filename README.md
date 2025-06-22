

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
Run the model_client.py to load the keras model directly, it sends some hardcoded test data.  
Or skip right to the "Start the Flask server" for the more full featured experience.

### Start the Flask Server 

venv\Scripts\activate       # or source venv/bin/activate on macOS/Linux
python serve_ekg_autoencoder.py

The server will run at `http://127.0.0.1:5000`.

Run the flask_client.py.  It opens a random record from normal.csv and anomaly.csv, prints the result to
the console.  The Flask server posts the result to its webpage.  If local ttp://127.0.0.1:5000, if the Flask
server is on a remote machine, you can view it by <Remote Machine URL>:5000 as below:

 "EKG Predictions Dashboard".  
Example:

2025-06-18 05:13:10
Prediction: [0.09907367825508118, -0.042691461741924286, 0.5079333186149597, 0.1889864206314087, 0.5483210682868958 ...]
Error: 0.5520787835121155
Anomaly: False

---
License: GPL v.2
