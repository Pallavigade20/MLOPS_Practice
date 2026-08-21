import joblib

# Load the trained model
model = joblib.load("model.pkl")

# Get user input
temperature = float(input("Temperature: "))
humidity = float(input("Humidity: "))
wind_speed = float(input("Wind Speed: "))

# Prepare input data
new_data = [[temperature, humidity, wind_speed]]

# Predict
prediction = model.predict(new_data)

# Display result
if prediction[0] == 1:
    print("\nPrediction: RAIN")
else:
    print("\nPrediction: NO RAIN")