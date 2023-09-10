import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Function to generate random date within a given range
def random_date(start, end):
    return start + timedelta(
        seconds=random.randint(0, int((end - start).total_seconds()))
    )


# Parameters
num_rows = 500
start_date = datetime(2020, 1, 1)
end_date = datetime(2023, 12, 31)
product_ids = range(1001, 1101)  # 100 different product IDs
countries = ["US", "CA", "UK", "AU", "DE"]

# Generate data
data = {
    "Date": [random_date(start_date, end_date) for _ in range(num_rows)],
    "Product_ID": [random.choice(product_ids) for _ in range(num_rows)],
    "Price": [round(random.uniform(20, 49), 2) for _ in range(num_rows)],
    "Quantity_Sold": [random.randint(1, 100) for _ in range(num_rows)],
    "Sale_Country_Code": [random.choice(countries) for _ in range(num_rows)],
}

# Create dataframe
df = pd.DataFrame(data)

# Save to CSV
file_path = "./sales_data.csv"
df.to_csv(file_path, index=False)

file_path
