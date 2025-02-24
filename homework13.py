'''
Homework13
Name: Ana Maya
github link: https://github.com/anamaya2/Python/blob/main/homework13.py
'''
def calculate_interest(principal, rate, time):
    interest = (principal * rate * time)
    return int(interest)

def compound_interest(principal, rate, n, time, ):
    amount = principal * (1 + rate / n) ** (n * time)
    compound_interest = amount - principal
    return (round(compound_interest,2))


if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest13.py'))
