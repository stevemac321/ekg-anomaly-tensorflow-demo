# This Python file uses the following encoding: utf-8
import sys
import json
import requests
import pandas as pd
import numpy as np
import random

from PySide6.QtWidgets import QApplication, QWidget

# You need to run this command beforehand to generate ui_form.py from your .ui file:
# pyside6-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

class EKGSimulator(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        # Connect buttons to functions
        self.ui.sendNormal.clicked.connect(self.send_ekg_normal_data)
        self.ui.sendAnom.clicked.connect(self.send_ekg_anom_data)

        # Load ECG data once
        self.load_data()

    def load_data(self):
        try:
            self.dataframe = pd.read_csv('ecg.csv', header=None)
            raw_data = self.dataframe.values
            self.signals = raw_data[:, :-1]
            self.labels = raw_data[:, -1]

            # Labels: 1 = Normal, 0 = Anomaly (Abnormal)
            self.normal_signals = self.signals[self.labels == 1]
            self.anomaly_signals = self.signals[self.labels == 0]

            print(f"Loaded {len(self.normal_signals)} normal and {len(self.anomaly_signals)} anomaly samples.")
        except Exception as e:
            print(f"Error loading ecg.csv: {e}")
            self.normal_signals = np.array([])
            self.anomaly_signals = np.array([])

    def send_ekg_normal_data(self):
        if len(self.normal_signals) == 0:
            print("No normal signals loaded.")
            return
        sample = random.choice(self.normal_signals).tolist()
        self.send_sample(sample)

    def send_ekg_anom_data(self):
        if len(self.anomaly_signals) == 0:
            print("No anomaly signals loaded.")
            return
        sample = random.choice(self.anomaly_signals).tolist()
        self.send_sample(sample)

    def send_sample(self, sample):
        ekg_data = {"input": sample}
        try:
            response = requests.post(
                "http://10.0.0.224:5000/predict",
                headers={"Content-Type": "application/json"},
                data=json.dumps(ekg_data)
            )
            print("Status Code:", response.status_code)
            print("Response JSON:", response.json())
        except Exception as e:
            print("Error sending EKG data:", e)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = EKGSimulator()
    print("Before show")
    widget.show()
    print("After show")
    sys.exit(app.exec())
