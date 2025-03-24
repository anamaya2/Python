'''
Homework24
Name: Ana Maya
github link: 
'''

def is_valid_password(word):
    pass

def is_between_8_and_20(password):
    length_of_password = len(password)
    if length_of_password < 8 and length_of_password > 20:
        return False
    else:
        return True
    
def has_uppercase(password):
    for letter in password:
        if letter.isupper():
            return True
    return False

def has_lowercase(password):
    for letter in password:
        if letter.islower():
            return True
    return False

def has_digit(password):
    for letter in password:
        if letter.isdigit():
            return True
    return False

def has_special_character(password):
    special_characters = "!@#$%^&*()-+"
    for letter in password:
        if letter in special_characters:
            return True
    return False

def is_valid_password(password):
    if is_between_8_and_20(password) and has_uppercase(password) and has_lowercase(password) and has_digit(password) and has_special_character(password):
        return True
    else:
        return False
    

def main():
    user_input = input("Enter a password: ")
    print(is_between_8_and_20(user_input))
    print(has_uppercase(user_input))
    print(has_lowercase(user_input))
    print(has_digit(user_input))
    print(has_special_character(user_input))
    print(is_valid_password(user_input))


if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest24.py'))