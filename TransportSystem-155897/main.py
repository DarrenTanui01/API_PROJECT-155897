from vehicle import Vehicle
from airport import Airport
from seaport import Seaport
from route import Route
from car_rental import CarRental

class Main:
    def __init__(self):
        self.vehicles = []
        self.airports = []
        self.seaports = []
        self.routes = []
        self.car_rentals = []

    def add_route(self):
        origin = input("Enter origin: ")
        destination = input("Enter destination: ")
        price = float(input("Enter price: "))
        departure_time = input("Enter departure time: ")
        route = Route(origin, destination, price, departure_time)
        self.routes.append(route)
        print(f"Route from {origin} to {destination} added successfully!")

    def add_car_rental(self):
        car_model = input("Enter car model: ")
        daily_rate = float(input("Enter daily rate: "))
        car_rental = CarRental(car_model, daily_rate)
        self.car_rentals.append(car_rental)
        print(f"Car rental {car_model} added successfully!")

    def rent_car(self):
        car_model = input("Enter car model to rent: ")
        for car in self.car_rentals:
            if car.car_model == car_model:
                if car.available:
                    days = int(input("Enter number of days to rent: "))
                    print(car.rent(days))
                else:
                    print(f"{car_model} is not available for rent.")
                return
        print(f"Car model {car_model} not found.")

    def return_car(self):
        car_model = input("Enter car model to return: ")
        for car in self.car_rentals:
            if car.car_model == car_model:
                print(car.return_car())
                return
        print(f"Car model {car_model} not found.")

    def book_trip(self):
        origin = input("Enter origin: ")
        destination = input("Enter destination: ")
        trip_type = input("Enter trip type (one-way/return): ").lower()

        matching_routes = [r for r in self.routes if r.origin == origin and r.destination == destination]
        
        if not matching_routes:
            print("No matching routes found.")
            return

        print("Available routes:")
        for i, route in enumerate(matching_routes):
            print(f"{i + 1}. {route.get_info()}")

        choice = int(input("Select a route (enter number): ")) - 1
        selected_route = matching_routes[choice]

        total_price = selected_route.price
        if trip_type == "return":
            total_price *= 2

        print(f"Booking confirmed: {selected_route.get_info()}")
        print(f"Trip type: {trip_type.capitalize()}")
        print(f"Total price: ${total_price}")

    def add_vehicle(self):
        name = input("Enter vehicle name: ")
        capacity = int(input("Enter vehicle capacity: "))
        self.vehicles.append(Vehicle(name, capacity))
        print(f"Vehicle {name} added successfully!")

    def add_airport(self):
        name = input("Enter airport name: ")
        location = input("Enter airport location: ")
        self.airports.append(Airport(name, location))
        print(f"Airport {name} added successfully!")

    def add_seaport(self):
        name = input("Enter seaport name: ")
        location = input("Enter seaport location: ")
        self.seaports.append(Seaport(name, location))
        print(f"Seaport {name} added successfully!")

    def update_vehicle(self):
        name = input("Enter vehicle name to update: ")
        for vehicle in self.vehicles:
            if vehicle._name == name:
                capacity = int(input("Enter new vehicle capacity: "))
                vehicle.update_capacity(capacity)
                print(f"Vehicle {name} updated successfully!")
                return
        print(f"Vehicle {name} not found!")

    def update_airport(self):
        name = input("Enter airport name to update: ")
        for airport in self.airports:
            if airport._name == name:
                location = input("Enter new airport location: ")
                airport.location = location
                print(f"Airport {name} updated successfully!")
                return
        print(f"Airport {name} not found!")

    def update_seaport(self):
        name = input("Enter seaport name to update: ")
        for seaport in self.seaports:
            if seaport._name == name:
                location = input("Enter new seaport location: ")
                seaport.location = location
                print(f"Seaport {name} updated successfully!")
                return
        print(f"Seaport {name} not found!")

    def delete_vehicle(self):
        name = input("Enter vehicle name to delete: ")
        for vehicle in self.vehicles:
            if vehicle._name == name:
                self.vehicles.remove(vehicle)
                print(f"Vehicle {name} deleted successfully!")
                return
        print(f"Vehicle {name} not found!")

    def delete_airport(self):
        name = input("Enter airport name to delete: ")
        for airport in self.airports:
            if airport._name == name:
                self.airports.remove(airport)
                print(f"Airport {name} deleted successfully!")
                return
        print(f"Airport {name} not found!")

    def delete_seaport(self):
        name = input("Enter seaport name to delete: ")
        for seaport in self.seaports:
            if seaport._name == name:
                self.seaports.remove(seaport)
                print(f"Seaport {name} deleted successfully!")
                return
        print(f"Seaport {name} not found!")

    def show_all(self):
        print("\n--- All Routes ---")
        for route in self.routes:
            print(route.get_info())

        print("\n--- All Car Rentals ---")
        for car in self.car_rentals:
            print(car.get_info())

        print("\n--- All Vehicles ---")
        for vehicle in self.vehicles:
            print(vehicle.get_info())

        print("\n--- All Airports ---")
        for airport in self.airports:
            print(airport.get_info())

        print("\n--- All Seaports ---")
        for seaport in self.seaports:
            print(seaport.get_info())

    def run(self):
        while True:
            print("\n1. Add Vehicle")
            print("2. Add Airport")
            print("3. Add Seaport")
            print("4. Update Vehicle")
            print("5. Update Airport")
            print("6. Update Seaport")
            print("7. Delete Vehicle")
            print("8. Delete Airport")
            print("9. Delete Seaport")
            print("10. Book a Trip")
            print("11. Add Route")
            print("12. Add Car Rental")
            print("13. Rent a Car")
            print("14. Return a Car")
            print("15. Show all")
            print("16. Exit")

            choice = input("Choose an option: ")

            if choice == '1':
                self.add_vehicle()
            elif choice == '2':
                self.add_airport()
            elif choice == '3':
                self.add_seaport()
            elif choice == '4':
                self.update_vehicle()
            elif choice == '5':
                self.update_airport()
            elif choice == '6':
                self.update_seaport()
            elif choice == '7':
                self.delete_vehicle()
            elif choice == '8':
                self.delete_airport()
            elif choice == '9':
                self.delete_seaport()
            elif choice == '10':  # Book a Trip
                self.book_trip()
            elif choice == '11': # Add Route
                self.add_route()
            elif choice == '12':  # Add Car Rental
                self.add_car_rental()
            elif choice == '13':  # Rent a Car
                self.rent_car()
            elif choice == '14':  # Return a Car
                self.return_car()
            elif choice == '15':
                self.show_all()
            elif choice == '16':
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

# This should be at the bottom of the file
if __name__ == "__main__":
    transport_system = Main()
    transport_system.run() 
    