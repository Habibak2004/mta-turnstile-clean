# scripts/transform.py

import pandas as pd
import os

def transform_turnstile_data():
    file_name = "Turnstile2022.csv"
    input_path = f"data/raw/{file_name}"
    output_path = f"data/processed/cleaned_{file_name}"

    try:
        # Load the CSV file
        df = pd.read_csv(input_path)
        # Clean column names: strip spaces and convert to uppercase
        df.columns = [col.strip().upper() for col in df.columns]

        print(f"✅ Loaded file with shape: {df.shape}")
    except Exception as e:
        print(f"❌ Error loading file: {e}")
        return

    # Show column names to inspect structure
    print("🔍 Columns:", df.columns.tolist())

    # Check for required columns
    required_cols = ['C/A', 'UNIT', 'SCP', 'DATE', 'TIME', 'ENTRIES']
    for col in required_cols:
        if col not in df.columns:
            print(f"⚠️ Missing expected column: {col}")
            return

    # Create a datetime column
    df['DATETIME'] = pd.to_datetime(df['DATE'] + ' ' + df['TIME'])

    # Sort and calculate hourly entries
    df = df.sort_values(['C/A', 'UNIT', 'SCP', 'DATETIME'])
    df['PREV_ENTRIES'] = df.groupby(['C/A', 'UNIT', 'SCP'])['ENTRIES'].shift(1)
    df['HOURLY_ENTRIES'] = df['ENTRIES'] - df['PREV_ENTRIES']

    # Filter out anomalies
    df = df[df['HOURLY_ENTRIES'].between(0, 5000)]
    print(f"📊 Rows after cleaning: {df.shape[0]}")

    # Save cleaned data
    os.makedirs("data/processed", exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"✅ Cleaned data saved to {output_path}")

if __name__ == "__main__":
    transform_turnstile_data()
