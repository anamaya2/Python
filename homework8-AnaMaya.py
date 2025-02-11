'''
Homework8
Name: Ana Maya
github link:https://github.com/anamaya2/Python/blob/main/homework8-AnaMaya.py
'''

def sum_numbers(lst):
    sum = 0
    # Create for loop to iterate through the list
    for num in lst:
        sum+= num
    return sum

def largest_number(lst):
    largest = lst[0]
    # Create for loop to iterate through the list
    for num in lst:
        # Check if the current number is greater than the largest number found so far
        if num > largest:
            largest = num
    return largest

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest8.py'))
