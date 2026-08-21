import pandas as pd
import joblib
from pathlib import Path
from sklearn.tree import DecisionTreeClassifier
import mlflow
import mlflow.sklearn

print("Training AI Model...")

# -------------------------------------------------------
# Read Feature Store
# -------------------------------------------------------
df = pd.read_csv("../data/customer_features.csv")

# -------------------------------------------------------
# Create Target Column
# 0 = Normal Billing
# 1 = Billing Anomaly
# -------------------------------------------------------
df["BillingStatus"] = [0, 0, 1, 0, 1, 0, 0, 1]

# -------------------------------------------------------
# Select Features
# -------------------------------------------------------
X = df[["MonthlyDataUsage", "AverageCallCount", "MonthlyBill", "UsageBillingRatio"]]
y = df["BillingStatus"]

# -------------------------------------------------------
# Train Model
# -------------------------------------------------------
model = DecisionTreeClassifier()
model.fit(X, y)

print("AI Model Trained Successfully")

# -------------------------------------------------------
# Save Model Locally
# -------------------------------------------------------
BASE = Path(__file__).resolve().parent.parent
model_folder = BASE / "models"
model_folder.mkdir(exist_ok=True)

joblib.dump(model, model_folder / "billing_model.pkl")

print("Model saved successfully")
print("Location :", model_folder / "billing_model.pkl")

# -------------------------------------------------------
# Log and Register Model in MLflow
# -------------------------------------------------------
mlflow.set_experiment("VodafoneBillingAI")

with mlflow.start_run():
    # Log parameters and metrics
    mlflow.log_param("model_type", "DecisionTreeClassifier")
    mlflow.log_metric("training_accuracy", model.score(X, y))

    # Log and register model
    mlflow.sklearn.log_model(
        model,
        artifact_path="billing_model",
        registered_model_name="RegressionModel"
    )

print("Model logged and registered in MLflow")


