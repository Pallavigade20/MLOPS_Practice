# app.py for endPoint 
from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)
model = joblib.load("local_model.pkl")

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
    app.run(port=5000, debug=True)
