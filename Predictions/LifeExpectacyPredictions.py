import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Load the CSV file
# Note: Skip the first 2 rows which contain metadata
data = pd.read_csv('..data\lifeexpectancy.csv', skiprows=2)

# Select rows that contain life expectancy data
life_exp_data = data[data['Indicator Name'] == 'Life expectancy at birth, total (years)']

# Extract years from columns
year_columns = [col for col in life_exp_data.columns if col.isdigit()]

# Create a dataframe to store year and average life expectancy
yearly_averages = pd.DataFrame(columns=['Year', 'Average Life Expectancy'])

# Calculate average life expectancy for each year across all countries
for year in year_columns:
    avg_life_exp = life_exp_data[year].mean(skipna=True)
    yearly_averages = yearly_averages._append({'Year': int(year), 
                                     'Average Life Expectancy': round(avg_life_exp)}, 
                                    ignore_index=True)

# Print the yearly averages
print("Yearly Average Life Expectancy (rounded to nearest whole number):")
print(yearly_averages.head())  # Show first few rows

# Prepare data for polynomial regression
X = yearly_averages['Year'].values.reshape(-1, 1)  # Reshape to 2D array
y = yearly_averages['Average Life Expectancy'].values

# Create polynomial features (degree 2)
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

# Split the data into training and testing sets
X_train_poly, X_test_poly, y_train, y_test = train_test_split(X_poly, y, test_size=0.2, random_state=42)

# Train the polynomial regression model
model = LinearRegression()
model.fit(X_train_poly, y_train)

# Make predictions on test data
y_pred = model.predict(X_test_poly)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f"\nMean Squared Error: {mse:.2f}")

# Display model coefficients
print(f"Model Coefficients: {model.coef_}")
print(f"Model Intercept: {model.intercept_:.2f}")

# Predict future values for the next 76 years (to 2100)
future_years = np.array(range(2025, 2101)).reshape(-1, 1)
future_years_poly = poly.transform(future_years)
future_predictions = model.predict(future_years_poly)

# Round predictions to nearest whole number
future_predictions = np.round(future_predictions)

# Create a dataframe with future predictions
future_df = pd.DataFrame({
    'Year': range(2025, 2101),
    'Predicted Life Expectancy': future_predictions
})

print("\nPredicted Future Life Expectancy (rounded to nearest whole number):")
print(future_df.head(10))  # Show first 10 rows