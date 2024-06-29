import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data from CSV file
df = pd.read_csv('sales_data.csv')

# Check the first few rows
print(df.head())

# Summary statistics
print(df.describe())

# Check for missing values
print(df.isnull().sum())

# Assume filling missing values with 0 for simplicity
df.fillna(0, inplace=True)

# Calculate total sales amount per product
df['TotalSales'] = df['UnitsSold'] * df['UnitPrice']

# Calculate total sales amount by year
df['OrderYear'] = pd.to_datetime(df['OrderDate']).dt.year
sales_by_year = df.groupby('OrderYear')['TotalSales'].sum()

# Plot total sales by year
plt.figure(figsize=(10, 6))
plt.plot(sales_by_year.index, sales_by_year.values, marker='o')
plt.xlabel('Year')
plt.ylabel('Total Sales ($)')
plt.title('Total Sales Over Years')
plt.grid(True)
plt.show()

# Example: Histogram of UnitPrice
plt.hist(df['UnitPrice'], bins=20, color='skyblue', edgecolor='black')
plt.xlabel('Unit Price')
plt.ylabel('Frequency')
plt.title('Histogram of Unit Price')
plt.show()

# Save processed data to CSV
df.to_csv('processed_sales_data.csv', index=False)
