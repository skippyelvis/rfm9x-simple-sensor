from rfm9x import RFM9X

class Receiver(RFM9X):
    
    def __init__(self, **kw):
        super().__init__(
            led=False, node=2, destination=1, name="sensor"
        )
        self.send("STARTUP:receiver")

    def poll(self):
        while True:
            packet = self.receive()
            if packet is not None:
                print(packet)

if __name__ == "__main__":
    recv = Receiver()
    recv.poll()
