'''
Homework2
Name: Ana Maya
github link: https://github.com/anamaya2/Python/edit/main/homework2%20-%20Ana%20Maya.py
'''

def inches_to_cm(inches):
    conversion = 2.54
    cm_value = inches * conversion
    return cm_value

def feet_to_meters(feet):
    conversion = 0.3048
    meters_value = feet * conversion
    return round(meters_value, 2)

def lbs_to_kg(lbs):
    conversion = 0.453592
    kg_value = lbs * conversion
    return round(kg_value, 2)

def hours_to_minutes(hrs):
    conversion = 60
    minutes_value = hrs * conversion
    return minutes_value

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest2.py'))


