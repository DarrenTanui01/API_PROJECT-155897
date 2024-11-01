from transport_network import TransportNetwork

class Airport(TransportNetwork):
    def __init__(self, name, location):
        super().__init__(name)
        self.location = location

    def get_info(self):
        return f"Airport: {self._name}, Location: {self.location}"