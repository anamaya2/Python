'''
Name: Ana Maya
GitHub Link: https://github.com/anamaya2/Python/blob/main/word_combinations.py
'''

# Generate the possible combinations of two letters. 
def two_letter_combinations(characters):
    for first in characters:
        for second in characters:
            yield first + second

# List the letters for combinations to be created
def main():
    letters = ['l', 'm', 'n', 'o', 'p']

    # Print the combinations
    for combo in  two_letter_combinations(letters):
        print(combo)

main()
