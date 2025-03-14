"""
This program calculates prices for custom house signs.
"""

# Charge for this sign.
charge = 0.0
# Number of characters on sign.
numChars = int(input("Enter the number of characters on the sign: "))
# Color of characters.
color = input("Enter the color of the characters (gold, black, or white): ")
# Type of wood.
woodType = woodType = input("Enter the type of wood (oak or pine): ")

# Write assignment and if statements here as appropriate.
# Base charge.
charge = 35.00
# Add charges for each additional character if more than 5.
if numChars > 5:
    charge += (numChars - 5) * 4.00
# Add charges for gold-leaf lettering.
if color == "gold":
    charge += 15.00
# Add charges for oak wood.
if woodType == "oak":
    charge += 20.00

# Output Charge for this sign.
print("The charge for this sign is $" + str(charge))