'''
Homework7
Name: Ana Maya
github link: https://github.com/anamaya2/Python/edit/main/homework7-AnaMaya.py
'''


def fizzbuzz(num):
    # Create loop
    for i in range(1, num + 1):
        # Check if number is divisible by 3, 5, or both
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0 and not i % 5 == 0:
            print("Fizz")
        elif i % 5 == 0 and not i % 3 == 0:
            print("Buzz")
        # If number is not divisible by 3 or 5, print the number
        else:
            print(i)

def scholarship_eligibility(gpa,credits):
    # Check if gpa is greater than or equal to 3.5 and credits are greater than or equal to 60
    if gpa >= 3.5 and credits >= 60:
        return True
    else:
        return False
    return

def max_of_three_numbers(num1,num2,num3):
    # Check which number is the largest
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
    return

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest7.py'))
