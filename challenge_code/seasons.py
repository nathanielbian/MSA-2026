# Create a decision structure to determine the season
# Winter, spring, summer, fall
# Ask the user to enter the number of the month. Month must be 1 - 12
# Output the season

def get_month():
    # Loop to collect valid input
    while True:
        # Try except block to catch a type error
        try:
            # Collect month input
            month = int(input("Enter month number: "))

            # Return the month if the value is valid
            if month in range(1, 13):
                return month

            # Print error message
            print("Error: Please enter a number 1 - 12!\n")
        except:
            # Print error message
            print("Error: Please enter a valid integer!\n")

def main():
    # Call get_month function
    month = get_month()

    # Check the month and output the season
    if month in range(3, 6):
        print("The season is spring.")
    elif month in range(6, 9):
        print("The season is summer.")
    elif month in range(9, 12):
        print("The season is fall.")
    else:
        print("The season is winter.")

# Call the main function
main()
