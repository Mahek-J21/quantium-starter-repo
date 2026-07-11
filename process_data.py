import pandas as pd
import os

# List of CSV files
files = [
    "data/daily_sales_data_0.csv",
    "data/daily_sales_data_1.csv",
    "data/daily_sales_data_2.csv"
]

# Empty list to store processed data
all_data = []

for file in files:
    # Read CSV
    df = pd.read_csv(file)

    # Keep only Pink Morsel rows
    df = df[df["product"] == "pink morsel"]

    # Remove the $ sign from price and convert to float
    df["price"] = df["price"].replace("[$]", "", regex=True).astype(float)

    # Calculate sales
    df["Sales"] = df["price"] * df["quantity"]

    # Keep only required columns
    df = df[["Sales", "date", "region"]]

    # Rename columns
    df.columns = ["Sales", "Date", "Region"]

    all_data.append(df)

# Combine all files
final_df = pd.concat(all_data, ignore_index=True)

# Save output
final_df.to_csv("formatted_output.csv", index=False)

print("Data processing completed successfully!")