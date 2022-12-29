from rfm9x import RFM9X
import time

def read_sensor():
    val = time.monotonic()
    return str(val)

class Sensor(RFM9X):

    def __init__(self, **kw):
        super().__init__(
            led=False, node=1, destination=2, name="sensor"
        )
        self.send("STARTUP:sensor")

    def poll(self):
        interval = 5
        now = time.monotonic()
        counter = 0
        while True:
            if time.monotonic() - now <= interval:
                continue
            counter += 1
            now = time.monotonic()
            val = read_sensor()
            msg = f"VAL:{val}-C:{counter}"
            print(msg)
            self.send(msg)

if __name__ == "__main__":
    sens = Sensor()
    sens.poll()
