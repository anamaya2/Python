'''
Homework5
Name: Ana Maya
github link: https://github.com/anamaya2/Python/blob/main/homework5-AnaMaya.py
'''

def collatz_conjecture(num):
    num=float(num)
    # While loop to check if num is not equal to 1
    while num!=1:
        print(num)
        if num%2==0:
            num=num/2
        else:
            num=3*num+1
    else:
        print(num)
    return 

def add_numbers(num):
    num=int(num)
    sum=0
    while num>1:
        num-=1
        sum+=num
    print(sum)
    return

if __name__ == "__main__":
        # Left these in for testing. Not sure if they're needed or not.
    # collatz_conjecture(6)
    # collatz_conjecture(18)
    # add_numbers(10)
    # add_numbers(25)

    import doctest
    print(doctest.testfile('doctest5.py'))
