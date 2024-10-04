import pandas as pd
import glob
import time

# Find All file with format csv
files = glob.glob("*.csv")

rows = input("Masukkan Nama Rows: ")
print('\n')

# Filetering Data
dfs = [pd.read_csv(file) for file in files]
combined_df = pd.concat(dfs, ignore_index=True)

# Deleted Rows Null 
combined_df = combined_df.dropna(how='all')

# Sort Data
combined_df = combined_df.sort_values(by=f'{rows}')

# Save Data Result
combined_df.to_csv('data.csv', index=False)

with open('data.csv', 'r', encoding="utf-8") as text:
    result = text.read()

# convert to list output
for index, row in combined_df.iterrows():
    print(row.tolist())
    time.sleep(0.1)