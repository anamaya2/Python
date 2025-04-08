'''
Homework1
Name: Ana Maya
github link:
Note: Remember to use comments for each function.
doc strings should include what each input consists of, 
what the expected output is and a description of the function.
'''

class Bank_Account:
    def __init__(self,name,starting_amount):
        self.name = name
        self.account = starting_amount
        
    
    def __repr__(self):
        return f"Bank_Account(name='{self.name}', Account Balance={self.account})"
    
    def __str__(self):
        return f"Account Name: {self.name}\nAccount Balance: {self.account}"
    #Prints information about the account.
    
    def deposit(self,amount):
        if amount > 0:
            self.account += amount
            print(f"{amount} deposited. New balance: {self.account}")
        else:
            print("Please deposit a positive number.")
        #Makes sure that the amount being deposited is positive and returns the appropriate text. 
    
    def withdraw(self,amount):
        if amount > 0:
            if amount <= self.account:
                self.account -= amount
                print(f"{amount} withdrawn. New balance: {self.account}")
            else:
                print("Insufficient funds.")
        else:
            print("Please withdraw an amount greater than zero.")
        #Makes sure that the amount being withdrawn is positive and returns the appropriate text.

    
    def check_balance(self):
        print(f"Balance: {self.account}")
        #Prints the balance of the account.

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest1.py'))