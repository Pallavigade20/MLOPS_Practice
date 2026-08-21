from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load trained model
model = joblib.load("model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    temperature = float(request.form["temperature"])
    humidity = float(request.form["humidity"])
    wind_speed = float(request.form["wind_speed"])

    prediction = model.predict(
        [[temperature, humidity, wind_speed]]
    )

    if prediction[0] == 1:
        result = "RAIN"
        emoji = "🌧️"
    else:
        result = "NO RAIN"
        emoji = "☀️"

    return render_template(
        "index.html",
        result=result,
        emoji=emoji
    )

if __name__ == "__main__":
    app.run(debug=True)