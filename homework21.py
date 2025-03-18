'''
Homework21
Name: Ana Maya
github link: https://github.com/anamaya2/Python/main/homework21.py
'''
def is_palindrome(string):
    cleaned_string = ''.join(char.lower() for char in string if char.isalnum())
    return cleaned_string == cleaned_string[::-1]
    
def is_anagram(string1,string2):
    cleaned_string1 = ''.join(char.lower() for char in string1 if char.isalnum())
    cleaned_string2 = ''.join(char.lower() for char in string2 if char.isalnum())
    return sorted(cleaned_string1) == sorted(cleaned_string2)

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest21.py'))
