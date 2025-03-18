'''
Homework20
Name: Ana Maya
github link: 
'''

def convert_to_ascii(string):
    if len(string) == 1:
        return ord(string)
    else:
        return [ord(char) for char in string]
    
def filter_non_ascii(string):
    return ''.join([char for char in string if ord(char) < 128])
    

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest20.py'))