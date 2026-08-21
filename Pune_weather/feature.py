import pandas as pd

# Load the dataset
df = pd.read_csv("pune_weather.csv")

# Convert Rain labels to numeric values
df["Rain"] = df["Rain"].map({
    "Yes": 1,
    "No": 0
})

# Create Features (X)
X = df[["Temperature", "Humidity", "WindSpeed"]]

# Create Target (y)
y = df["Rain"]

# Display Features
print("FEATURES (X)")
print(X)

# Display Target
print("\nTARGET (y)")
print(y)