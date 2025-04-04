# program calculates profits and sales prices for a furniture company

itemName = "TV Stand"
retailPrice = 325.00
wholesalePrice = 200.00

# calculate profit
profit = retailPrice - wholesalePrice

# calculate sales price with 25% off
salesPrice = retailPrice * 0.75

# calculate profit when sales price is used
saleProfit = salesPrice - wholesalePrice

# display results
print("Item Name: " + itemName)
print("Retail Price: $" + str(retailPrice))
print("Wholesale Price: $" + str(wholesalePrice))
print("Profit: $" + str(profit))
print("Sales Price: $" + str(salesPrice))
print("Profit from Sale: $" + str(saleProfit))






