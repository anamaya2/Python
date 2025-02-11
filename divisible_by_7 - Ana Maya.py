'''
Homework6
Name: Ana Maya
github link: https://github.com/anamaya2/Python/blob/main/divisible_by_7%20-%20Ana%20Maya.py
'''

def div_by_seven(num):
    for i in range(1, num):
        if i % 7 == 0:
            print(i)
    return 

def squares_of_numbers(num):
    sum = 0
    for i in range(1, num):
        print(i**2)
        sum += i**2
    # print("The sum of squares from 1 to " + str(num) + " is " + str(sum))
    # ^ I made that a comment because it is not in the doctest6.py file. It does work though.
    return 

if __name__ == "__main__":
    squares_of_numbers(3)
    # import doctest
    # print(doctest.testfile('doctest6.py'))
