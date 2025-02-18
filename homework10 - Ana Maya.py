'''
Homework10
Name: Ana Maya
github link:
'''

def find_missing_number(lst):
    lst.sort()
    missing_numbers = []
    for num in range(0, lst[-1] + 1):
        if num not in lst:
            missing_numbers.append(num)
    return missing_numbers

def even_partition(lst):
    even_numbers = []
    for num in lst:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest10.py'))