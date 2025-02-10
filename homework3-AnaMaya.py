'''
Homework3
Name: Ana Maya
github link:
'''

def positive_or_negative(num):
    print(num > 0)
    return 

def is_able_to_drive(num):
    print(num >= 16)
    return

def is_able_to_vote(num):
    print(num >= 18)
    return

def can_buy_alcohol(num):
    print(num >= 21)  
    return 

def senior_discount(num):
    print(num >= 65)
    return 

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest3.py', verbose=True))