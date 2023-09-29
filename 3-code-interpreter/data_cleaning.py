import pandas as pd

# 1. Load the CSV file into a DataFrame
sales_data = pd.read_csv("/mnt/data/sales_data.csv")

# 2. Remove rows with missing information and create a copy of the resulting DataFrame
cleaned_sales_data = sales_data.dropna().copy()

# 3. Fix the incorrect separator in the Date column
cleaned_sales_data['Date'] = cleaned_sales_data['Date'].str.replace(';', ':')

# 4. Convert the Date column to datetime64
cleaned_sales_data['Date'] = pd.to_datetime(cleaned_sales_data['Date'])

# 5. Convert the Product_ID and Quantity_Sold columns to int64
cleaned_sales_data['Product_ID'] = cleaned_sales_data['Product_ID'].astype(int)
cleaned_sales_data['Quantity_Sold'] = cleaned_sales_data['Quantity_Sold'].astype(int)

# 6. Fix inconsistencies in the Price column and convert it to float64
cleaned_sales_data['Price'] = cleaned_sales_data['Price'].str.replace('"', '')
cleaned_sales_data['Price'] = cleaned_sales_data['Price'].astype(float)

# 7. Remove any remaining rows with missing data
final_cleaned_sales_data = cleaned_sales_data.dropna()
