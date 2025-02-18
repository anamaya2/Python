'''
Homework11
Name:  Ana Maya
github link:
'''

def count_zeros(lst):
    count = 0
    for row in lst:
        for num in row:
            if num == 0:
                count += 1
    return count

def replace_with_zero(lst):
    for row in lst:
        for num in row:
            if num < 0:
                row[row.index(num)] = 0
    return lst

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest11.py'))