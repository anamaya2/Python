'''
Homework23
Name: Ana Maya
github link: 
'''

def group_by_first_letter(words):
    grouped = {}
    for word in words:
        first_letter = word[0].lower()
        if first_letter not in grouped:
            grouped[first_letter] = []
        grouped[first_letter].append(word)
    return grouped

def convert_to_sentence(words):
    sentence = ' '.join(words)
    return sentence + '.'


if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest23.py'))