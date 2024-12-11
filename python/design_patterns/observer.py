from enum import Enum

class HandshakeEvent(Enum):
    INIT = 0,
    START = 1,
    SUCCESS = 2,
    FAILURE = 3

class Observable():
    def __init__(self):
        self.callbacks = []

    def subscribe(self, callback):
        self.callbacks.append(callback)

    def notify(self, e: HandshakeEvent):
        for observer in self.callbacks:
            observer(e)

class Server(Observable):
    def handshake_started(self):
        self.notify(HandshakeEvent.START)

    def handshake_completed(self):
        self.notify(HandshakeEvent.SUCCESS)

class Client:
    def __init__(self, server: Server):
        server.subscribe(self.event_handler)
    
    def event_handler(self, e: HandshakeEvent):
        if e == HandshakeEvent.INIT:
            print("Handshake not yet started")
        elif e == HandshakeEvent.START:
            print("Handshake started")
        elif e == HandshakeEvent.SUCCESS:
            print("Handshake successful")
        elif e == HandshakeEvent.FAILURE:
            print("Handshake failed")

if __name__ == "__main__":
    server = Server()
    client = Client(server)

    server.handshake_started()
    server.handshake_completed()
