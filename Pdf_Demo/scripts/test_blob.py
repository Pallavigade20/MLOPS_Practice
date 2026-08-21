from blob_utils import download_blob

print("Testing Azure Blob Storage...")

download_blob(
    "raw-data/billing_data.csv",
    "../data/billing_data.csv"
)

print("Blob access successful!")