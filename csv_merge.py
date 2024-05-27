import pandas as pd

# Define file paths
file_paths = [
    "DOGEUSDT-1d-2020-07.csv",
    "DOGEUSDT-1d-2020-08.csv",
    "DOGEUSDT-1d-2020-09.csv",
    "DOGEUSDT-1d-2020-10.csv",
    "DOGEUSDT-1d-2020-11.csv",
    "DOGEUSDT-1d-2020-12.csv",
    "DOGEUSDT-1d-2021-01.csv",
    "DOGEUSDT-1d-2021-02.csv",
    "DOGEUSDT-1d-2021-03.csv",
    "DOGEUSDT-1d-2021-2024.csv"
]

# Load and concatenate CSV files
dfs = [pd.read_csv(file) for file in file_paths]
merged_df = pd.concat(dfs)

# Save the merged dataframe to a new CSV file
output_path = "DOGEUSDT-1d-2020-2024.csv"
merged_df.to_csv(output_path, index=False)

output_path
