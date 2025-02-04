'''
Homework2
Name: Ana Maya
github link: 
'''

def birthday(month: str, day: int, year: int) -> str:
    """
    Inputs: month: string, day: int, year: int
    Output: a string
    Description: This function generates a personalized message for the user based on the provided birthday.
    """
    return f"Your birthday is {month} {day}, {year}."

def address(street: str, city: str, state: str, zipcode: int) -> str:
    """
    Inputs: street: string, city: string, state: string, zipcode: int
    Output: a string
    Description: This function generates a personalized message for the user based on the provided address.
    """
    return f"Your address is {street}, {city}, {state}, {zipcode}."

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest25.py'))