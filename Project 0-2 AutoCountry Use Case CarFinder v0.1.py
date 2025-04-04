# AutoCountry Vehicle Finder v0.1
#Allowed Vehicles List
AllowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']

# print show menu
def show_menu():
    print("\n********************************")
    print("AutoCountry Vehicle Finder v0.1")
    print("********************************")
    print("Please Enter the following number below from the following menu:") 
    print("1. PRINT all Authorized Vehicles")  # Print the full list of authorized vehicles
    print("2. SEARCH for a Vehicle")  # Search for a specific vehicle in the list
    print("3. Exit") # Exit the program

#print allowed vehicles
def print_vehicles():
    print("\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    for vehicle in AllowedVehiclesList:
        print(vehicle) # Display each vehicle in the list

# Function to search for a vehicle in AllowedVehiclesList
def search_vehicle():
    search = input("\nEnter the name of the vehicle you want to search for: ") # Get user input for vehicle name
    if search in AllowedVehiclesList:  # Check if the vehicle is in the list
        print(f"\nThe vehicle '{search}' is authorized for purchase.")  # Vehicle found message
    else:
        print(f"\nThe vehicle '{search}' is NOT authorized for purchase.")  # Vehicle not found message

# Main program loop to display the menu and handle user input until exit
while True:
    show_menu() # Display the menu
    choice  = input("\nEnter your choice: ") # Get user input for menu choice
    
# Handle user choice
    if choice == "1":
        print_vehicles()  # Print the list of authorized vehicles
    elif choice == "2":
        search_vehicle()  # Call function to search for a vehicle
    elif choice == "3":
        print("\nThank you for using the AutoCountry Vehicle Finder, good-bye!")   # Exit the program
        break  # Exit the loop and end the program
    else:
        print("\nInvalid choice, please try again.")  # Handles invalid input