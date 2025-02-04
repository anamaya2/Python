
'''
Name: Ana
GitHub Link: https://github.com/anamaya2/Python/blob/main/Input%20Homework.py
'''
# Getting the users total budget
totalBudget = float(input("Please enter your total budget: "))

# Getting the users spending in each category
housing = float(input("Enter the total spending amount for the following cateogories:\nHousing: "))
utilities = float(input("Utilities: "))
groceries = float(input("Groceries: "))
transportation = float(input("Transportation: "))
healthCare = float(input("Health Care: "))
personalCare = float(input("Personal Care: "))
clothing = float(input("Clothing: "))
debt = float(input("Debt: "))

# Calculating the percentages of the total budget spent in each category
housingPercentage = (housing / totalBudget) * 100
utilitiesPercentage = (utilities / totalBudget) * 100
groceriesPercentage = (groceries / totalBudget) * 100
transportationPercentage = (transportation / totalBudget) * 100
healthCarePercentage = (healthCare / totalBudget) * 100
personalCarePercentage = (personalCare / totalBudget) * 100
clothingPercentage = (clothing / totalBudget) * 100
debtPercentage = (debt / totalBudget) * 100

# Printing the results
print(f"Your total budget is: {totalBudget}")
print("Your spending in each category is as follows:")
print(f"Housing: {housing} ({housingPercentage:.2f}% of the total budget)")
print(f"Utilities: {utilities} ({utilitiesPercentage:.2f}% of the total budget)")
print(f"Groceries: {groceries} ({groceriesPercentage:.2f}% of the total budget)")
print(f"Transportation: {transportation} ({transportationPercentage:.2f}% of the total budget)")
print(f"Health Care: {healthCare} ({healthCarePercentage:.2f}% of the total budget)")
print(f"Personal Care: {personalCare} ({personalCarePercentage:.2f}% of the total budget)")
print(f"Clothing: {clothing} ({clothingPercentage:.2f}% of the total budget)")
print(f"Debt: {debt} ({debtPercentage:.2f}% of the total budget)")

