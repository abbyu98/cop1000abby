# AutoCountry Vehicle Finder v0.1
#Allowed Vehicles List
AllowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']

# print show menu
def show_menu():
    print("\n********************************")
    print("AutoCountry Vehicle Finder v0.1")
    print("********************************")
    print("Please Enter the following number below from the following menu:")
    print("1. PRINT all Authorized Vehicles")
    print("2. Exit")

#print vehicles
def print_vehicles():
    print("\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    for vehicle in AllowedVehiclesList:
        print(vehicle)

# Main program loop to display the menu and handle user input
while True:
    show_menu()
    choice = input("\nEnter your choice: ")
    
# Handle user choice
    if choice == "1":
        print_vehicles()  # Print the list of authorized vehicles
    elif choice == "2":
        print("\nThank you for using the AutoCountry Vehicle Finder, good-bye!")  # Exit the program
    else:
        print("\nInvalid choice, please try again.")  # Handle invalid input











