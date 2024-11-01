# TransportSystem

TransportSystem is a Python-based project that simulates a transportation network, including various modes of transport, routes, and passenger management.

Also run it from the terminal if the output section is not working.

## Project Structure

The project consists of several Python classes:

- `TransportNetwork`: An abstract base class for different types of transport networks.
- `Route`: Represents a route with origin, destination, price, and departure time.
- `Vehicle`: Represents a vehicle in the transport network, capable of carrying passengers.
- `Seaport`: A specific type of transport network for sea-based transportation.
- `Passenger`: Represents a passenger in the transport system.

## Features

- Add and remove passengers from vehicles
- Manage vehicle capacity and availability
- Create and manage routes within the transport network
- Specialized transport networks (e.g., Seaport)
- Get information about vehicles, routes, and transport networks

## Usage

Here's a basic example of how to use the TransportSystem:

```python
# from vehicle import Vehicle
# from passenger import Passenger
# from route import Route

# Create a vehicle
# bus = Vehicle("City Bus", 50)

# Add passengers
# passenger1 = Passenger("Alice")
# passenger2 = Passenger("Bob")
# bus.add_passenger(passenger1)
# bus.add_passenger(passenger2)

# Create a route
#route = Route("Downtown", "Suburb", 5.00, "09:00 AM")

# Add route to vehicle
bus.add_route(route)

# Get vehicle info
#print(bus.get_info())