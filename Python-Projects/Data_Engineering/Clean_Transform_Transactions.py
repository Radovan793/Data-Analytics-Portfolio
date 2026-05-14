import pandas as pd

# Step 1: Load data
df = pd.read_csv("transactions_sample.csv")

# Step 2: Drop rows with missing client_id or amount
df.dropna(subset=["client_id", "amount"], inplace=True)

# Step 3: Clean column names
df.columns = df.columns.str.strip().str.lower()

# Step 4: Standardize text values
df['currency'] = df['currency'].str.upper()
df['status'] = df['status'].str.lower()

# Step 5: Parse mixed-format dates
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Step 6: Keep only 'cleared' transactions
df = df[df['status'] == 'cleared']

# Step 7: Normalize amounts to EUR
conversion_rates = {'EUR': 1, 'USD': 0.9, 'GBP': 1.1}
df['amount_eur'] = df.apply(
    lambda row: row['amount'] * conversion_rates.get(row['currency'], 1),
    axis=1
)

# Step 8: Final tidy output
df.reset_index(drop=True, inplace=True)

# Step 9: Save cleaned data (optional)
df.to_csv("transactions_cleaned.csv", index=False)

print(df.head())
