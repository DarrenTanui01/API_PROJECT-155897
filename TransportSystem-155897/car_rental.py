class CarRental:
    def __init__(self, car_model, daily_rate):
        self.car_model = car_model
        self.daily_rate = daily_rate
        self.available = True

    def rent(self, days):
        if self.available:
            self.available = False
            return f"Rented {self.car_model} for {days} days. Total cost: ${self.daily_rate * days}"
        else:
            return f"{self.car_model} is not available for rent."

    def return_car(self):
        self.available = True
        return f"{self.car_model} has been returned and is now available for rent."

    def get_info(self):
        status = "Available" if self.available else "Not Available"
        return f"Car: {self.car_model}, Daily Rate: ${self.daily_rate}, Status: {status}"