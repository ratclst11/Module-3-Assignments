# Define the Vehicle class
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

# Define the Automobile class that inherits from Vehicle
class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)  # Initialize the vehicle_type attribute from the Vehicle class
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

# Main function to run the app
def main():
    # Set the vehicle type to "car"
    vehicle_type = "car"
    
    # Get user input for the car details
    year = input("Enter the year of the car: ")
    make = input("Enter the make of the car: ")
    model = input("Enter the model of the car: ")
    doors = input("Enter the number of doors (2 or 4): ")
    roof = input("Enter the type of roof (solid or sun roof): ")

    # Create an instance of Automobile with the user input
    car = Automobile(vehicle_type, year, make, model, doors, roof)

    # Output the data in an easy-to-read format
    print("\nVehicle Information:")
    print(f"  Vehicle type: {car.vehicle_type}")
    print(f"  Year: {car.year}")
    print(f"  Make: {car.make}")
    print(f"  Model: {car.model}")
    print(f"  Number of doors: {car.doors}")
    print(f"  Type of roof: {car.roof}")

# Run the main function
if __name__ == "__main__":
    main()