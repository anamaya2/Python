'''
Name: Ana Maya
GitHub Link:
'''

class NotNumericError(Exception):
    def __init__(self, message="Input must be a number."):
        self.message = message
        super().__init__(self.message)

def main():

    #Get user input
    while True:
        try:
            user_input = input("Please enter a number: ")

            # Check if the input is numeric
            if not user_input.isnumeric():
                raise NotNumericError("The input provided is not a valid number.")
            
        except NotNumericError as e:
            print(f"Error: {e}")

        else:
            print(f"You entered a valid number: {user_input}")
            break
    
        finally:
            print("Attempt to enter a number completed.")


main()
