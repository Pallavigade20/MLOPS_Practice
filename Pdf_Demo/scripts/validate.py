import pandas as pd
from blob_utils import download_blob

print("=== TEST RT-001 - Validate Raw Data ===")

#download_blob("raw-data/billing_data.csv", "billing_data.csv")
df = pd.read_csv("../data/billing_data.csv")

required_columns = ["CustomerID","DataGB","Calls","BillAmount"]
missing_columns = [c for c in required_columns if c not in df.columns]

if missing_columns:
    print("FAIL - Missing columns:", missing_columns)
else:
    print("PASS - Required columns exist")

if df[required_columns].isnull().sum().sum() == 0:
    print("PASS - No missing values")
else:
    print("FAIL - Missing values found")

if df["CustomerID"].duplicated().sum() == 0:
    print("PASS - No duplicate CustomerID")
else:
    print("FAIL - Duplicate CustomerID found")
