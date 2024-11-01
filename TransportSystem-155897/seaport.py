from transport_network import TransportNetwork

class Seaport(TransportNetwork):
    def __init__(self, name, location):
        super().__init__(name)
        self.location = location

    def get_info(self):
        return f"Seaport: {self._name}, Location: {self.location}"