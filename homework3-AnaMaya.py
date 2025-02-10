'''
Homework3
Name: Ana Maya
github link: https://github.com/anamaya2/Python/edit/main/homework3-AnaMaya.py
'''

# Check if the number is positive or negative
def positive_or_negative(num):
    if num > 0:
        print("The number is positive.")
    else:
        print("The number is negative.")
    return 

# Check if the user is able to drive
def is_able_to_drive(num):
    if num >= 16:
        print("User is able to drive.")
    else:
        print("User is not able to drive.")
    return

# Check if the user is able to vote
def is_able_to_vote(num):
    if num >= 18:
        print("User is able to vote.")
    else:
        print("User is not able to vote.")
    return

# Check if the user can buy alcohol
def can_buy_alcohol(num):
    if num >= 21:
        print("User can buy alcohol.")
    else:
        print("User cannot buy alcohol.") 
    return 

# Check if the user is eligible for senior discount
def senior_discount(num):
    if num >= 55:
        print("User is eligible for senior discount.")
    else:
        print("User is not eligible for senior discount.")
    return 

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest3.py', verbose=True))


