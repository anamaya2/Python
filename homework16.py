'''
Homework16
Name: Ana Maya
github link:
'''

def pythagorean_thm(tuple):
    a, b = tuple
    result = (a**2 + b**2)**0.5
    # Next part is to return integers as integers and float numbers with decimals. 
    if result == int(result):
        return int(result)
    else:
        return round(result, 2)

def distance_between_points(tuple1,tuple2):
    x1, y1 = tuple1
    x2, y2 = tuple2
    result = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    # Next part is also to return integers as integers and float numbers with decimals. 
    if result == int(result):
        return int(result)
    return round(result, 2)

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest16.py'))