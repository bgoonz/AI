import pandas as pd
# Given data
P = 12000  # annual payment (12 months * $1000/month)
r = 0.08  # annual interest rate
n = 38  # number of years
# Initialize variables
years = list(range(1, n + 1))
invested_start = [0] * n
invested_end = [0] * n
current_value = [0] * n
interest_year = [0] * n
total_interest = [0] * n

# Initialize values for the first year
invested_end[0] = P
current_value[0] = P * (1 + r)
interest_year[0] = current_value[0] - invested_end[0]
total_interest[0] = interest_year[0]

# Calculate values for each subsequent year
for i in range(1, n):
    invested_start[i] = invested_end[i-1]
    invested_end[i] = invested_start[i] + P
    current_value[i] = (invested_end[i] + current_value[i-1]) * (1 + r)
    interest_year[i] = current_value[i] - current_value[i-1] - P
    total_interest[i] = total_interest[i-1] + interest_year[i]

# Create a dataframe to display the results
df = pd.DataFrame({
    'Year': years,
    'Invested Start of Year ($)': invested_start,
    'Invested End of Year ($)': invested_end,
    'Current Value End of Year ($)': current_value,
    'Interest Gained This Year ($)': interest_year,
    'Total Interest Gained ($)': total_interest
})

print(df)
