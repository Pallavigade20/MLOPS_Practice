import pickle
import pandas as pd

# Load the trained model
with open("models/covid_model.pkl", "rb") as file:
    model = pickle.load(file)

# -----------------------------------------
# Enter New Patient Details
# -----------------------------------------
age = 60
temperature = 39.2
oxygen = 90
cough_days = 7
comorbidity = 1

# -----------------------------------------
# Feature Engineering
# -----------------------------------------
TemperatureAboveNormal = 1 if temperature > 38 else 0
LowOxygen = 1 if oxygen < 94 else 0
LongCough = 1 if cough_days >= 5 else 0

# -----------------------------------------
# Create Input DataFrame
# -----------------------------------------
patient = pd.DataFrame({
    "Age": [age],
    "TemperatureAboveNormal": [TemperatureAboveNormal],
    "LowOxygen": [LowOxygen],
    "LongCough": [LongCough],
    "Comorbidity": [comorbidity]
})

# -----------------------------------------
# Predict
# -----------------------------------------
prediction = model.predict(patient)

# -----------------------------------------
# Display Result
# -----------------------------------------
if prediction[0] == 1:
    print("Prediction: Covid")
else:
    print("Prediction: Not Covid")

print("\nPatient Details:")
print(patient)
