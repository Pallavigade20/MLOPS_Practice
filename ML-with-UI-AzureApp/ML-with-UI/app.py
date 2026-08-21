# app.py for endPoint 
from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd
import os

app = Flask(__name__)
# model = joblib.load("local_model.pkl")
model = joblib.load(os.path.join(os.path.dirname(__file__), "local_model.pkl"))


@app.route("/")
def index():
    return render_template("chat.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    df = pd.DataFrame([data])
    prediction = model.predict(df)[0]
    result = "Normal Billing" if prediction == 0 else "Billing Anomaly Detected"
    return jsonify({"response": result})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # default 5000 locally
    app.run(host="0.0.0.0", port=port)
