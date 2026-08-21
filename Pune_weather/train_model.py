import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load dataset
data = pd.read_csv("pune_weather.csv")

# Features
X = data[["Temperature", "Humidity", "WindSpeed"]]

# Target
y = data["Rain"].map({
    "Yes": 1,
    "No": 0
})

# Split data into 80% training and 20% testing
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# Create Logistic Regression model
model = LogisticRegression()

# Train model
model.fit(X_train, y_train)

# Save trained model
joblib.dump(model, "model.pkl")

print("Model trained successfully.")
print("Model saved as model.pkl")