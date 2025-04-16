# AutoCountry Vehicle Finder v0.1

#Allowed Vehicles File
 AllowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan', 'Rivian R1T', 'Ram 1500' ]

# print show menu
def show_menu():
    print("\n********************************")
    print("AutoCountry Vehicle Finder v0.1")
    print("********************************")
    print("Please Enter the following number below from the following menu:") 
    print("1. PRINT all Authorized Vehicles")  # Print the full list of authorized vehicles
    print("2. SEARCH for a Vehicle")  # Search for a specific vehicle in the list
    print("3. ADD a Vehicle")  # Allow Sales Manager to add a vehicle
    print("4. REMOVE a Vehicle")  # Allow Sales Manager to remove a vehicle
    print("5. Exit") # Exit the program

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

# Function to add a new vehicle to AllowedVehiclesList
def add_vehicle():
    new_vehicle = input("\nEnter the name of the vehicle you want to add: ")  # Get user input for new vehicle
    if new_vehicle in AllowedVehiclesList:
        print(f"\nThe vehicle '{new_vehicle}' is already authorized.")  # Inform user if vehicle already exists
    else:
        AllowedVehiclesList.append(new_vehicle)  # Add vehicle to the list
        print(f"\nThe vehicle '{new_vehicle}' has been successfully added to the authorized list.")  # Success message

# Function to remove a vehicle from AllowedVehiclesList (Only for Sales Manager)
def remove_vehicle():
    user_role = input("\nEnter your role (Sales Manager required): ")  # Get user role
    if user_role.lower() == "sales manager":
        vehicle_to_remove = input("\nEnter the name of the vehicle you want to remove: ")  # Get vehicle to remove
        if vehicle_to_remove in AllowedVehiclesList:
             confirm = input(f"\nAre you sure you want to remove \"{vehicle_to_remove}\" from the Authorized Vehicles List? (yes/no): ")
             if confirm.lower() == "yes":
                AllowedVehiclesList.remove(vehicle_to_remove)  # Remove vehicle from the list
                print(f"\nThe vehicle '{vehicle_to_remove}' has been successfully removed from the authorized list.")  # Success message
        else:
            print(f"\nThe vehicle '{vehicle_to_remove}' is not found in the list.")  # Vehicle not in list message
    else:
        print("\nAccess Denied! Only Sales Managers can remove vehicles.")  # Access control message



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
        add_vehicle()   # Call function to add a new vehicle
    elif choice == "4":
        remove_vehicle()  # Call function to remove a vehicle
    elif choice == "5":
        print("\nThank you for using the AutoCountry Vehicle Finder, good-bye!")
        break  # Exit the loop and end the program
    else:
        print("\nInvalid choice, please try again.")  # Handles invalid input