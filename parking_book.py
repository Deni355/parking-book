total_spots = [1, 2, 3, 4, 5] # Total parking spots
not_avaible = [] # Booked parking spots
cars = [] # List of car objects

class Vehicle():
    def __init__(self, spot, license, model):
        self.spot = spot
        self.license = license
        self.model = model

    def info(self):
        print(f"\nVehicle information:")
        print(f"License: {self.license}")
        print(f"Model: {self.model}")
        print(f"Parking spot: {self.spot}")

def display_spots(): # Display the parking spots
    print("\nParking spots:\n")

    for spot in total_spots: # Loop through the total spots
        status = "Booked" if spot in not_avaible else "Available"
        print(f"Parking Spot {spot} = {status}")

def book_spot(): # Book a parking spot
    display_spots()
    spot = int(input("\nChoose a spot: "))
    if spot in not_avaible: # Check if the spot is already booked
        print("This spot is already booked")
        return again()

    print("\nEnter vehicle details: ")
    license = input("License: ") # Get the license plate
    
    # Check if the license is already booked
    for car in cars:
        if car.license == license:
            print("This car is already booked")
            return again()
    
    model = input("Model: ") # Get the model of the car
    print(f"\nYou have chosen parking spot {spot}")
    print(f"Vehicle Details:\nLicense Plate: {license}\nModel: {model}")
    
    print("Please check if everything is correct.")
    print("\nDo you want to confirm?")
    answer = input("Y/N: ")
    
    if answer == "Y" or answer == "y":
        car = Vehicle(spot, license, model) # Create a new car object
        not_avaible.append(spot) # Add the booked spot to the not_avaible list
        cars.append(car) # Add the car object to the cars list
        print("Booking confirmed!")
    elif answer == "N" or answer == "n":
        print("Booking cancelled!")
    else:
        print("Invalid input")
    

def edit_booking(): # Edit the booking
    license = input("\nWrite the license plate of the car you want to edit: ")

    for car in cars: # Loop through the cars list
        if car.license == license:
            print("\nWhat do you want to edit?")
            print(f"1. License Plate = {car.license}")
            print(f"2. Model = {car.model}")
            print(f"3. Parking spot = {car.spot}")
            option = int(input("\nChoose an option: "))

            if option == 1:
                new_license = input("Enter a new license: ")
                car.license = new_license # Change the license plate of the car
                print("\nLicense plate edited!")
                print(f"New license plate: {car.license}")
            elif option == 2:
                new_model = input("Enter a new model: ")
                car.model = new_model # Change the model of the car
                print("\nModel edited!")
                print(f"New model: {car.model}")
            elif option == 3:
                display_spots() # Show the available spots
                new_spot = int(input("Choose a new spot: "))
                if new_spot in not_avaible: # Check if the spot is already booked
                    print("\nThis spot is already booked")
                    return again()
                else:
                    not_avaible.remove(car.spot) # Remove the old spot from the not_avaible list
                    car.spot = new_spot # Change the spot of the car
                    not_avaible.append(new_spot) 
                    print("\nSpot edited!")
                    print(f"New spot: {car.spot}")
            else:
                print("Invalid input")
            return # Exit after editing the car
        else:
            print("\nCar not found")
            return again()

def cancel_booking(): # Cancel the booking
    license = input("\nWrite the license plate of the car you want to cancel: ")

    for car in cars: # Loop through the cars list
        if car.license == license: # Check if the car is found
            print("\nAre you sure you want to cancel the booking?")
            answer = input("Y/N: ")

            if answer == "Y" or answer == "y":
                print("Booking cancelled!")
                not_avaible.remove(car.spot) # Remove the booked spot from the not_avaible list
                cars.remove(car) # Remove the car object from the cars list
            elif answer == "N" or answer == "n":
                print("Booking not cancelled!")
            else:
                print("Invalid input")
            return # Exit after cancelling the booking
        else:
            print("\nCar not found")
            return again()

def information(): # Get information about the car
    print("\nInformation:")
    print("1. Search by License Plate")
    print("2. Search by Parking spot")

    option = int(input("\nChoose an option: "))

    if option == 1:
        license = input("Enter the license plate: ")
        found = False # Check if the car is found

        for car in cars: # Loop through the cars list
            if car.license == license: # Check if the license plate is found
                car.info() # Display the car information
                found = True
                break
        if not found:
            print("Car not found")

    elif option == 2:
        spot = int(input("Enter the parking spot: "))
        found = False
        
        for car in cars:
            if car.spot == spot: # Check if the spot is found
                car.info()
                found = True
                break
        if not found:
            print("Car not found")

    else:
        print("Invalid input")

def again(): # Ask the user if they want to continue
    print("\nDo you want to continue?")
    answer = input("Y/N: ")

    if answer == "Y" or answer == "y":
        main_menu()
    elif answer == "N" or answer == "n":
        print("Goodbye!")
        exit()
    else:
        print("Invalid input")

def main_menu(): # Main menu
    print("\nParking management system")
    print("1. View parking spots")
    print("2. Book a parking spot")
    print("3. Edit booking")
    print("4. Cancel booking")
    print("5. Information")
    print("6. Exit")

    option = int(input("\nChoose an option: "))
    if (option == 1):
        display_spots()
        again()
    elif (option == 2):
        book_spot()
        again()
    elif (option == 3):
        edit_booking()
        again()
    elif (option == 4):
        cancel_booking()
        again()
    elif (option == 5):
        information()
        again()
    elif (option == 6):
        print("Goodbye!")
        exit()
    else:
        print("Invalid input")
        again()

main_menu() # Start the program
