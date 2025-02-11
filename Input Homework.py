
'''
Name: Ana
GitHub Link: https://github.com/anamaya2/Python/blob/main/Input%20Homework.py
'''
# Getting the user's total budget
totalBudget = float(input("Please enter your total budget: "))

# Getting the user's spending in each category
housing = float(input("Enter the total spending amount for the following categories:\nHousing: "))
utilities = float(input("Utilities: "))
groceries = float(input("Groceries: "))
transportation = float(input("Transportation: "))
healthCare = float(input("Health Care: "))
personalCare = float(input("Personal Care: "))
clothing = float(input("Clothing: "))
debt = float(input("Debt: "))

# Calculate total spending
totalSpending = housing + utilities + groceries + transportation + healthCare + personalCare + clothing + debt

# Calculating percentages based on total spending
housingPercentage = (housing / totalSpending) * 100
utilitiesPercentage = (utilities / totalSpending) * 100
groceriesPercentage = (groceries / totalSpending) * 100
transportationPercentage = (transportation / totalSpending) * 100
healthCarePercentage = (healthCare / totalSpending) * 100
personalCarePercentage = (personalCare / totalSpending) * 100
clothingPercentage = (clothing / totalSpending) * 100
debtPercentage = (debt / totalSpending) * 100

# Printing results
print(f"\nYour total budget is: ${totalBudget:.2f}")
print(f"Your total spending is: ${totalSpending:.2f}")
    
print("\nYour spending in each category is as follows:")
print(f"Housing: ${housing:.2f} ({housingPercentage:.2f}% of total spending)")
print(f"Utilities: ${utilities:.2f} ({utilitiesPercentage:.2f}% of total spending)")
print(f"Groceries: ${groceries:.2f} ({groceriesPercentage:.2f}% of total spending)")
print(f"Transportation: ${transportation:.2f} ({transportationPercentage:.2f}% of total spending)")
print(f"Health Care: ${healthCare:.2f} ({healthCarePercentage:.2f}% of total spending)")
print(f"Personal Care: ${personalCare:.2f} ({personalCarePercentage:.2f}% of total spending)")
print(f"Clothing: ${clothing:.2f} ({clothingPercentage:.2f}% of total spending)")
print(f"Debt: ${debt:.2f} ({debtPercentage:.2f}% of total spending)")

