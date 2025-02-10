'''
Homework4
Name: Ana Maya
github link:
'''

def grade_calculator(score):
    # Checks to make sure the score is between 0 and 100 and prints the grade letter 
    if 0<=score and score<=100:
        if score>=90:
            print("'A'")
        elif score>=80:
            print("'B'")
        elif score>=70:
            print("'C'")
        elif score>=60:
            print("'D'")
        else:
            print("'F'")
    else:
        print("'Enter a grade between 0-100'")
    return

    # Checks to see if the number is even or odd and prints the result
def even_or_odd(num):
    if num % 2 == 0:
        print("'even'")
    else:
        print("'odd'")
    return 



if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest4.py', verbose=True))