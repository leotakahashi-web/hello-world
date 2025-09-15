# Electric Charges Program

# Prompt user for kilowatt hours used
kwh = int(input("Enter the KW hours used: "))

# Rates (cents per kWh)
rate_first_1000 = 7.633 / 100   # convert cents to dollars
rate_over_1000 = 9.259 / 100    # convert cents to dollars

# Calculate bill using branching
if kwh <= 1000:
    amount_owed = kwh * rate_first_1000
else:
    amount_owed = (1000 * rate_first_1000) + ((kwh - 1000) * rate_over_1000)

# Print result
print("Amount owed is $", round(amount_owed, 5))