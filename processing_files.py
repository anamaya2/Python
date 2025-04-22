'''
Name: Ana Maya
GitHub Link:
'''

def main():

    
    try:
        # Open the file
        file = open("sales_totals.txt", "r")

        total = 0.0
        count = 0

        # Read the file and start adding numbers together
        for line in file:
            line = line.strip()
            number = float(line)
            total += number
            count += 1
            print(f"{number:.2f}")

        file.close()

        # Calculate the average
        if count > 0:
            average = total / count
        else: average = 0.0

        # Print the results
        print(f"\nTotal: {total:,.2f}")
        print(f"Number of entries: {count}")
        print(f"Average: {average:,.2f}")


    except FileNotFoundError:
        print("The file was not found.")
    except Exception as e:
        print("an error ocurred:", e)

main()
