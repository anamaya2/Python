'''
Homework17
Name: Ana Maya
github link: https://github.com/anamaya2/Python/blob/main/homework17.py
'''


def frequency_counter(lst):
    frequency = {}
    for item in lst:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    result = ",".join(f"{key}:{value}" for key,value in frequency.items())
    return frequency
# For some reason I can't make the spaces that appear in the terminal go away. Tried different ways and tried debugging with ChatGPT but I couldn't fix it. 

def translation(english_words):
    phonetic_alphabet = {
        'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta',
        'E': 'Echo', 'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel',
        'I': 'India', 'J': 'Juliett', 'K': 'Kilo', 'L': 'Lima',
        'M': 'Mike', 'N': 'November', 'O': 'Oscar', 'P': 'Papa',
        'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango',
        'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'X-ray',
        'Y': 'Yankee', 'Z': 'Zulu'
    }
    translation = []
    english_words = english_words.upper()
    for letter in english_words:
        if letter in phonetic_alphabet:
            translation.append(phonetic_alphabet[letter])
        else:
            translation.append(letter)
    result = "\n".join(translation)
    print(result)

# Main function to test both features
if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest17.py'))  # Test the file with doctest
