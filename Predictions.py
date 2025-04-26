import pandas as pd

# Load the CSV file
csv_file_path = 'path_to_your_csv_file.csv'
data = pd.read_csv(csv_file_path)

# Display the first few rows of the CSV file
print(data.head())

# Example: Access specific columns
# Replace 'column_name' with the actual column name in your CSV
if 'column_name' in data.columns:
    specific_column = data['column_name']
    print(specific_column)