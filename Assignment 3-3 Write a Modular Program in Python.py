# Function: This program determines if a date entered by the user is valid.  
# Input statements to retrieve year, month, and day from the user
# Output: Valid date is printed or user is alerted that an invalid date was entered.

year = int(input("Enter a year: "))
month = int(input("Enter a month (1-12): "))
day = int(input("Enter a day (1-31): "))

# Validate the input
if year > 0 and 1 <= month <= 12 and 1 <= day <= 31:
    # If valid
    print(f"{month}/{day}/{year} is a valid date.")
else:
    # If invalid
    print(f"{month}/{day}/{year} is an invalid date.")

# end of program
