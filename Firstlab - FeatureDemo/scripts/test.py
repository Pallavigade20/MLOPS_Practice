import pandas as pd

# Load the two CSV files
df1 = pd.read_csv('../data/billing_data.csv')
df2 = pd.read_csv('../data/customer_features.csv')

# Find matching rows based on a specific common column (e.g., 'ID')
matched_rows = pd.merge(df1, df2, on='CustomerID', how='inner')

# Save matched rows to a new CSV file
matched_rows.to_csv('matched_output.csv', index=False)

print("all row matched")

def check_csv_for_nulls(file_path):
    df = pd.read_csv(file_path)
    
    # 1. Quick true/false check
    has_nulls = df.isnull().values.any()
    
    print(f"\n--- Analysis for {file_path} ---")
    if has_nulls:
        print("❌ Found missing values!")
        
        # 2. Show count of nulls per column
        print("\nMissing values per column:")
        print(df.isnull().sum())
        
        # 3. Optional: Show the specific rows that have nulls
        null_rows = df[df.isnull().any(axis=1)]
        print("\nRows with missing data:")
        print(null_rows)
    else:
        print("✅ Clean! No missing values found.")

# Run the check on your files
check_csv_for_nulls('../data/billing_data.csv')
check_csv_for_nulls('../data/customer_features.csv')

# Load your CSV file
file_path = '../data/customer_features.csv'
df = pd.read_csv(file_path)

# --- APPROACH A: Check for 100% identical rows ---
duplicate_rows = df[df.duplicated()]

# --- APPROACH B: Check duplicates in specific columns only ---
# Uncomment the line below to check just by an ID or Email column
# duplicate_rows = df[df.duplicated(subset=['ID_Column_Name'])]

print(f"--- Analysis for {file_path} ---")
if not duplicate_rows.empty:
    print(f"❌ Found {len(duplicate_rows)} duplicate records!\n")
    print("Here are the duplicate rows:")
    print(duplicate_rows)
    
    # Optional: Save duplicates to a new file to review them
    # duplicate_rows.to_csv('duplicates_found.csv', index=False)
else:
    print("✅ Clean! No duplicate records found.")

#Model reads customer_features.csv
import re
from pathlib import Path

def print_training_csv_name():
    # 1. Path to your training script
    training_script = "train_model.py"
    
    try:
        # 2. Read the text inside train_model.py
        with open(training_script, "r", encoding="utf-8") as file:
            content = file.read()
            
        # 3. Look for the pd.read_csv line
        match = re.search(r'pd\.read_csv\([\'"](.+?)[\'"]\)', content)
        
        if match:
            full_path = match.group(1)          # Extracts: ../data/customer_features.csv
            file_name = Path(full_path).name    # Extracts: customer_features.csv
            
            # 4. Print the final results
            print(f"📋 Training Script Analyzed: {training_script}")
            print(f"📁 Full Data Path Found:    {full_path}")
            print(f"🎯 CSV File Name Used:      {file_name}")
            return file_name
        else:
            print(f"❌ Could not find a 'pd.read_csv' line inside {training_script}.")
            
    except FileNotFoundError:
        print(f"❌ Error: The file '{training_script}' was not found in this folder.")

# Run the function
print_training_csv_name()

