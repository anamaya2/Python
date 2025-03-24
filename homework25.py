'''
Homework24
Name: Ana Maya
github link: https://github.com/anamaya2/Python/blob/main/homework25.py
'''

def flowers(idx,list_of_flowers):
    try:
        if idx > 0:
            print("You selected:", list_of_flowers[idx])
        else:
            print("You selected:", list_of_flowers[idx])
    except TypeError:
        print("Invalid input! Please enter a number.")
    except IndexError:
        print("Number out of range! Please choose a valid flower number.")

    


if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest25.py'))
