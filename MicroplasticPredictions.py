import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Load the CSV file
csv_file_path = 'data/Marine_Microplastics.csv'
data = pd.read_csv(csv_file_path)
data.dropna(inplace=True)  # Drop rows with missing values

# Display the first few rows of the CSV file
print(data.head())

# Select two properties (columns) from the dataset
X = pd.to_datetime(data['Date'], format='mixed').dt.year.values.reshape(-1, 1)  # Reshape to 2D array
y = data['Measurement'].values

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the polynomial regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Predict future values (e.g., for the next 100 years)
years = []
for i in range(2000, 2100):
    years.append(i)
future_years = pd.DataFrame({'Year': years})
future_predictions = model.predict(future_years.values.reshape(-1, 1))