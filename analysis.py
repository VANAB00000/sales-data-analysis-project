import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Show first rows
print(df.head())

# Data Cleaning
df.dropna(inplace=True)

# Total Sales
total_sales = df['Sales'].sum()
print("Total Sales:", total_sales)

# Top 5 Products
top_products = df.groupby('Sub-Category')['Sales'].sum().sort_values(ascending=False).head(5)
print(top_products)

# Region-wise Sales
region_sales = df.groupby('Region')['Sales'].sum()
print(region_sales)

# Plot 1: Top Products
plt.figure()
top_products.plot(kind='bar')
plt.title("Top 5 Products by Sales")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.show()

# Plot 2: Region Sales
plt.figure()
region_sales.plot(kind='pie', autopct='%1.1f%%')
plt.title("Region-wise Sales Distribution")
plt.ylabel("")
plt.show()
