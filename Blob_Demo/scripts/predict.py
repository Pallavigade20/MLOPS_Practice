import pandas as pd, joblib

print("=== VODAFONE BILLING PREDICTION ===")

model = joblib.load("../models/voismodel_v1.pkl")

new_customer = pd.DataFrame({
    "MonthlyDataUsage":[19],
    "AverageCallCount":[185],
    "MonthlyBill":[1480],
    "UsageBillingRatio":[0.0128]
})

prediction = model.predict(new_customer)

print("Prediction :", "Normal Billing" if prediction[0]==0 else "Billing Anomaly Detected")
