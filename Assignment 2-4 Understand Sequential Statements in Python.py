# Input statements to receive salary and number of dependents
salary = float(input("Enter salary: "))
numDependents = int(input("Enter number of dependents: "))

# Calculate state tax based on salary (6.5%)
stateTax = salary * 0.065

# Calculate federal tax based on salary (28%)
federalTax = salary * 0.28

# Calculate dependent deduction based on number of dependents (2.5% per dependent)
dependentDeduction = salary * (numDependents * 0.025)

# Calculate total withholdings by adding state tax, federal tax, and dependent deduction
totalDeductions = stateTax + federalTax + dependentDeduction

# Calculate take-home pay by subtracting total deductions from salary above
takeHomePay = salary - totalDeductions

# output statements
print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))
print("State Tax: $" + str(stateTax))
print("Federal Tax: $" + str(federalTax))
print("Dependent Deduction: $" + str(dependentDeduction))
print("Total Deductions: $" + str(totalDeductions))


