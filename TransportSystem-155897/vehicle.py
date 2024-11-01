from transport_network import TransportNetwork
from passenger import Passenger

class Vehicle(TransportNetwork):
    def __init__(self, name, capacity):
        super().__init__(name)
        self._capacity = capacity
        self._passengers = []
        self._availability = True

    def add_passenger(self, passenger):
        if len(self._passengers) < self._capacity:
            self._passengers.append(passenger)
            print(f"{passenger.name} added to {self._name}.")
        else:
            print(f"{self._name} is at full capacity!")

    def remove_passenger(self, passenger):
        if passenger in self._passengers:
            self._passengers.remove(passenger)
            print(f"{passenger.name} removed from {self._name}.")
        else:
            print(f"{passenger.name} is not on {self._name}.")

    def get_info(self):
        return f"Vehicle: {self._name}, Capacity: {self._capacity}, Passengers: {[p.name for p in self._passengers]}"

    def update_capacity(self, new_capacity):
        self._capacity = new_capacity

    def set_availability(self, availability):
        self._availability = availability

    def is_available(self):
        return self._availability