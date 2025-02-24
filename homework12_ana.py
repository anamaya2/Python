'''
Homework12
Name: Ana Maya
github link:
'''
def rectangle(side1,side2):
    area = side1 * side2
    return('The area of the rectangle is ' + str(area) + ' square units')

def circle(radius):
    area = 3.14 * radius * radius
    return('The area of a circle is ' + str(round(area,2)) + ' square units')   


if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest12.py'))


