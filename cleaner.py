import pandas as pd
import os

# Aapki file ka sahi naam yahan likha hai
input_file = '/app/data/car details v4.csv'
output_file = '/app/data/cleaned_car_data.csv'

if os.path.exists(input_file):
    # CSV read kar rahe hain
    df = pd.read_csv(input_file)
    print(f"--- Raw Data Loaded: {len(df)} rows ---")
    
    # 1. Cleaning: Jis row mein koi bhi value missing ho usay hata dein
    df_cleaned = df.dropna()
    
    # 2. Logic: Sirf 2015 ke baad wali gaadiyan filter karein
    if 'Year' in df_cleaned.columns:
        df_cleaned = df_cleaned[df_cleaned['Year'] >= 2015]
    
    # Save cleaned file
    df_cleaned.to_csv(output_file, index=False)
    print(f"--- Success! Cleaned file saved: {len(df_cleaned)} rows ---")
    print(f"✅ Filtered data available at: {output_file}")
else:
    print(f"❌ Error: {input_file} nahi mili. Check karein file name sahi hai?")