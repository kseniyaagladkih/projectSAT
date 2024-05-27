import pandas as pd

# Define file paths
file_paths = [
    "DOGEUSDT-1d-2024-01.csv",
    "DOGEUSDT-1d-2024-02.csv",
    "DOGEUSDT-1d-2024-03.csv",
    "DOGEUSDT-1d-2024-04.csv"
]

# Load and concatenate CSV files
dfs = [pd.read_csv(file) for file in file_paths]
merged_df = pd.concat(dfs)

# Save the merged dataframe to a new CSV file
output_path = "DOGEUSDT-1d-2024.csv"
merged_df.to_csv(output_path, index=False)

output_path
