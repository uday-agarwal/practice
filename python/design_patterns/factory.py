""" Router for network packets.

This module implements a Router class which handles
different types of network packets.
"""
from abc import ABC, abstractmethod

class Router(ABC):
    @abstractmethod
    def __init__(self, name: str):
        self.name = name
        self.BluetoothSupported = False

    def get_name(self):
        return self.name

class Cisco(Router):
    def __init__(self, name: str):
        super().__init__(name)
        self.LowBandSupported = True
        self.HighBandSupported = False

class Juniper(Router):
    def __init__(self, name: str):
        super().__init__(name)
        self.LowBandSupported = True
        self.HighBandSupported = True

class Mist(Router):
    def __init__(self, name: str):
        super().__init__(name)
        self.LowBandSupported = True
        self.HighBandSupported = True
        self.BluetoothSupported = True

class RouterFactory:
    """ Factory class for Router.
    
    Creates an instance of the Router class as per
    the user input.
    """
    def __init__(self):
        self._routers = {}

        # Read config and load _routers
        self.register_router('cisco', Cisco)
        self.register_router('juniper', Juniper)
        self.register_router('Mist', Mist)

    def register_router(self, name: str, router: Router):
        self._routers[name] = router

    def get_router(self, name: str):
        return self._routers[name]("Uday's router")

def run():
    router = router_factory.get_router('cisco')
    print(type(router))
    print(router.get_name())
    print(router.BluetoothSupported)

if __name__ == '__main__':
    router_factory = RouterFactory()
    run()

## Reading a config file - do we need to convert string to number etc.?
