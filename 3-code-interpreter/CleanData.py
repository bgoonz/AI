# Creating the Python script for data cleaning


import pandas as pd

def clean_sales_data(file_path):
    # Read the CSV file
    df = pd.read_csv(file_path)
    
    # Check for missing values and drop if any
    df.dropna(inplace=True)
    
    # Remove duplicate rows if any
    df.drop_duplicates(inplace=True)
    
    # Ensure all prices are within the range of $20 to $49
    df = df[(df['Price'] >= 20) & (df['Price'] <= 49)]
    
    # Ensure valid country codes
    valid_countries = ['US', 'CA', 'UK', 'AU', 'DE']
    df = df[df['Sale_Country_Code'].isin(valid_countries)]
    
    # Ensure that the "Quantity_Sold" column has only positive values
    df = df[df['Quantity_Sold'] > 0]
    
    return df

if __name__ == "__main__":
    # Example usage
    cleaned_data = clean_sales_data('/path/to/your/sales_data.csv')
    cleaned_data.to_csv('./sales_data.csv', index=False)
    print("Data cleaning completed and saved to './sales_data.csv'")



