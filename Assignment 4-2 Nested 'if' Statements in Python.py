"""
This program calculates an employee's productivity bonus based on their productivity score.
"""

# Enter Employee Name.
employee_name = input("Enter Employee Name: ")
# Enter number of shifts.
shifts = int(input("Enter number of shifts: "))
# Enter number of transactions.
transactions = int(input("Enter number of transactions: "))
# Enter transactions dollar value.
transactionValue = float(input("Enter transactions dollar value: "))

# Calculate productivity score
if shifts > 0 and transactions > 0:  
    productivity_score = (transactionValue / transactions) / shifts
else:
    productivity_score = 0

# Determine the bonus based on the productivity score
if productivity_score <= 30:
    bonus = 50.00
elif productivity_score <= 69:
    bonus = 75.00
elif productivity_score <= 199:
    bonus = 100.00
else:
    bonus = 200.00

# Print the results
print(f"Employee Name: {employee_name}")
print(f"Bonus: ${bonus:.2f}")