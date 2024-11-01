from abc import ABC, abstractmethod

class TransportNetwork(ABC):
    def __init__(self, name):
        self._name = name
        self._routes = []

    @abstractmethod
    def get_info(self):
        pass

    def add_route(self, route):
        self._routes.append(route)

    def get_routes(self):
        return self._routes