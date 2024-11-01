class Route:
    def __init__(self, origin, destination, price, departure_time):
        self.origin = origin
        self.destination = destination
        self.price = price
        self.departure_time = departure_time

    def get_info(self):
        return f"Route: {self.origin} to {self.destination}, Price: ${self.price}, Departure: {self.departure_time}"