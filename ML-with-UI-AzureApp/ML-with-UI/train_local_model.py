import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

# Tiny dataset
df = pd.DataFrame({
    "MonthlyDataUsage":[10,6,15,8],
    "AverageCallCount":[120,90,160,110],
    "MonthlyBill":[800,450,1200,650],
    "UsageBillingRatio":[0.012,0.013,0.012,0.012],
    "BillingStatus":[0,0,1,0]
})

X = df[["MonthlyDataUsage","AverageCallCount","MonthlyBill","UsageBillingRatio"]]
y = df["BillingStatus"]

model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

joblib.dump(model, "local_model.pkl")
print("Model saved as local_model.pkl")
