'''
Name: Ana Maya
GitHub Link: https://github.com/anamaya2/Python/blob/main/calendar_1.py
'''

import calendar
import datetime

def main():

    current_year = datetime.datetime.now().year

    while True:
        try:
            month = int(input("Enter your birth month (1-12): "))

            if 1<= month <= 12:
                print(f"Your birth month calendar is {calendar.month(current_year, month)}")
                break
            else:
                print("Please enter a valid month (1-12)")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 12.")

main()
