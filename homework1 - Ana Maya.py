'''
Homework1
Name: Ana Maya
github link: https://github.com/anamaya2/Python/blob/main/homework1%20-%20Ana%20Maya.py
'''

import random

def check(guess, actual_number):
    # Getting the difference between the guess and the actual number
    difference = abs(guess - actual_number)
    # Returning the appropriate text based on the guess
    if difference == 0:
        return "You Got It!"
    elif difference < 5:
        return "Very Hot"
    elif difference < 10:
        return "Hot"
    elif difference < 20:
        return "Cool"
    else:
        return "Cold"
    pass
    
def main(actual_number):
    actual_number = random.randint(1,100)
    
    while True:
        guess = int(input("Guess a number between 1 and 100: "))
        print(check(guess, actual_number))
        if check(guess, actual_number) == "You Got It!":
            break

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest1.py'))
