'''
Name: Ana Maya
GitHub Link: 
'''

import datetime

def main():
    try:

        birth_year = int(input("Enter your birth year: "))
        birth_month = int(input("Enter your birth month (1-12): "))
        birth_day = int(input("Enter your birth day (1-31): "))

        birthday = datetime.date(birth_year, birth_month, birth_day)


        today = datetime.date.today()

        age_in_days = (today - birthday).days
        age_in_years = age_in_days // 365.25
        age_in_months = age_in_years * 12 + (today.month - birthday.month)
        age_in_hours =  age_in_days * 24
        age_in_minutes = age_in_hours * 60

        print(f"Your age in days: {age_in_days}")
        print(f"Your age in years: {age_in_years:.2f}")
        print(f"Your age in months: {age_in_months:.2f}")
        print(f"Your age in hours: {age_in_hours}")
        print(f"Your age in minutes: {age_in_minutes}")


    except ValueError:
        print("Invalid input. Please enter valid numbers for year, month, and day.")
        return
    
main()


