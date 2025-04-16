# AutoCountry Vehicle Finder v0.1
#Allowed Vehicles File
VEHICLE_FILE = "vehicles.txt"

# Function to read allowed vehicles from file
def read_vehicles():
    try:
        with open(VEHICLE_FILE, "r") as file:
            vehicles = [line.strip() for line in file.readlines()]
        return vehicles
    except FileNotFoundError:
        return [] # Return an empty list if the file is not found
    
# Function to write updated allowed vehicles to file
def write_vehicles(vehicles):
    with open(VEHICLE_FILE, "w") as file:
        for vehicle in vehicles:
            file.write(vehicle + "\n")

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

# print allowed vehicles from file
def print_vehicles():
    vehicles = read_vehicles()
    if vehicles:
        print("\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
        for vehicle in vehicles:
            print(vehicle) # Display each vehicle in the list

# Function to search for a vehicle in the file
def search_vehicle():
    search = input("\nEnter the name of the vehicle you want to search for: ") # Get user input for vehicle name
    vehicles = read_vehicles()
    if search in vehicles:  # Check if the vehicle is in the list
        print(f"\nThe vehicle '{search}' is authorized for purchase.")  # Vehicle found message
    else:
        print(f"\nThe vehicle '{search}' is NOT authorized for purchase.")  # Vehicle not found message

# Function to add a new vehicle to the file
def add_vehicle():
    new_vehicle = input("\nEnter the name of the vehicle you want to add: ")  # Get user input for new vehicle
    vehicles = read_vehicles()
    if new_vehicle in vehicles:
        print(f"\nThe vehicle '{new_vehicle}' is already authorized.")  # Inform user if vehicle already exists
    else:
        vehicles.append(new_vehicle)  # Add vehicle to the list
        print(f"\nThe vehicle '{new_vehicle}' has been successfully added to the authorized list.")  # Success message

# Function to remove a vehicle from the file (Only for Sales Manager)
def remove_vehicle():
    user_role = input("\nEnter your role (Sales Manager required): ")  # Get user role
    if user_role.lower() == "sales manager":
        vehicles = read_vehicles()  # Read the current list of vehicles
        vehicle_to_remove = input("\nEnter the name of the vehicle you want to remove: ")  # Get vehicle to remove
        if vehicle_to_remove in vehicles:
             confirm = input(f"\nAre you sure you want to remove \"{vehicle_to_remove}\" from the Authorized Vehicles List? (yes/no): ")
             if confirm.lower() == "yes":
                vehicles.remove(vehicle_to_remove)  # Remove vehicle from the list
                write_vehicles(vehicles)
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