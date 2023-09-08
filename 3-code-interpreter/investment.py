# Given data
P = 12000  # annual payment (12 months * $1000/month)
r = 0.08  # annual interest rate
n = 38  # number of years

# Calculate the future value using the formula
FV = P * ((1 + r)**n - 1) / r


# Round the future value to two significant digits
FV_rounded = round(FV, -int(len(str(int(FV))) - 6))

print(FV_rounded)
