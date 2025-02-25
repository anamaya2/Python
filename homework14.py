'''
Homework14
Name: Ana Maya
github link: https://github.com/anamaya2/Python/blob/main/homework14.py
'''
lb_to_kg = 0.453592
inch_to_m = 0.0254


# If I make this program ask the user for input, it won't work with the doctest. 

def convert_to_kg(lbs):
    #Convers pounds to kilograms
    return round(lbs * lb_to_kg,2)

def convert_to_meters(inches):
    #Convert inches to meters
    return round(inches * inch_to_m,2)

def bmi_calculation(lbs,height):
    #Calculate BMI
    weight = convert_to_kg(lbs)
    height = convert_to_meters(height)
    bmi = round(weight / (height ** 2),2)
    if bmi < 18.5:
        return "underweight"
    elif 18.5 <= bmi < 24.9:
        return "normal weight"
    elif 25 <= bmi < 29.9:
        return "overweight"
    else:
        return "obese"

# I couldn't get the bmi_calculation function return the same things as the doctest. When I put the words in two quotations, (Ex. "normal weight"), it gave me an error and said it expected single quotations. 
# When I put the code in single quotations, it said it expected double quotations. I don't know how to fix this.

if __name__ == "__main__":
    import doctest
    print(doctest.testfile("doctest14.py"))
