import pandas as pd

# Load the dataset
data = pd.read_csv("data/diabetes.csv")

# Check the first 5 rows
print(data.head())

# Check number of rows and columns
print("\nShape (rows, columns):", data.shape)

# Check column names
print("\nColumns:", list(data.columns))

# Check for missing values
print("\nMissing values per column:\n", data.isnull().sum())

# Basic statistics
print("\nStatistics:\n", data.describe())