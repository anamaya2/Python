'''
Homework18
Name: Ana Maya
github link: https://github.com/anamaya2/Python/blob/main/homework18.py
'''

def iterate_dictionary(lst):
    dict = {1:"one",2:"two",3:"three"}
    for num in lst:
        try:
            print(dict[num])
        except:
            print("Number not in dictionary")
    return

def check_if_positive(lst):
    for num in lst:
        try:
            if num > 0:
                print(num)
            else:
                raise ValueError
        except ValueError:
            print("not positive")
    return

def division(lst):
    for num in lst:
        try:
            print(round(100/num,2))
        except ZeroDivisionError:
            print("can't divide by zero")
    return 

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest18.py'))
