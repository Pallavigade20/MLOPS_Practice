import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Read feature dataset
df = pd.read_csv("data/covid_features.csv")

# Input Features
X = df[
    [
        "Age",
        "TemperatureAboveNormal",
        "LowOxygen",
        "LongCough",
        "Comorbidity"
    ]
]

# Target
y = df["HighRisk"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Accuracy
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print(f"\nModel Accuracy: {accuracy:.2f}")

# Save Model
with open("models/covid_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model saved successfully")