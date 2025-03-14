'''
Homework9
Name: Ana Maya
github link: https://github.com/anamaya2/Python/blob/main/homework9%20-%20Ana%20Maya.py
'''

def bubble_sort(lst):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                swapped = True
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return lst

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest9.py'))
