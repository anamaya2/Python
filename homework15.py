'''
Homework15
Name:
github link:
'''
# Takes a number and returns its factorial
def factorial(n):
    if n== 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Takes factorial of a number and prints it
def main(num1):
    result = factorial(num1)
    print(f'"The factorial of {num1} is {result}."')
    return

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest15.py'))