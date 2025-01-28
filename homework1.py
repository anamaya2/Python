'''
Homework1
Name: Ana Maya
github link: 
'''

def add(num1,num2):
    print(num1+num2)
    return 

def subtract(num1,num2):
    print(num1-num2)
    return 

def multiply(num1,num2):
    print(num1*num2)
    return 

def division(num1,num2):
    print(num1/num2)
    return 

def int_div(num1,num2):
    print(num1//num2)
    return 

def modulus(num1,num2):
    print(num1%num2)
    return 

def exp(num1,num2):
    print(num1**num2)
    return 

def area(length,width):
    print("'The area of the rectangle with a length of" + " " + str(length) + " " + "and a width of" " " + str(width) + " " + "is " + str(length*width) + "'")
    return 


if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest1.py'))