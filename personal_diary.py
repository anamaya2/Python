'''
Name: Ana Maya
GitHub Link:
'''

def main():
    # Ask user for the date and time
    date_time = input("Please enter the date and time (Example: April 21, 2025 - 9:50 PM): ")
    
    # Let user write the diary entry
    entry = input("Please enter your diary entry: ")


    #Open the file and insert the entry
    try:
        file = open("diary.txt", "a")
    
        file.write("Date and Time: " + date_time + "\n")

        file.write("Entry: " + entry + "\n")

        file.write("\n")

        file.close()

        print("Your diary entry has been saved successfully!")

    except Exception as e:
        print("An error occurred:", e)

main()

