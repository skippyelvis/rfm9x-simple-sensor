import board
import busio
import digitalio
import adafruit_rfm9x

class RFM9X:
    
    def __init__(self, **kw):
        spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
        self.led = digitalio.DigitalInOut(board.D13)
        self.led.direction = digitalio.Direction.OUTPUT
        self.led.value = kw.get("led", False)
        cs = digitalio.DigitalInOut(board.RFM9X_CS)
        reset = digitalio.DigitalInOut(board.RFM9X_RST)
        self.radio = adafruit_rfm9x.RFM9x(spi, cs, reset, 915.0)
        self.radio.enable_crc = True
        self.radio.node = kw.get("node", None)
        self.radio.destination = kw.get("destination", None)
        self.name = kw.get("name", None)

    def send(self, msg):
        msg = bytes(msg, "UTF-8")
        self.radio.send(msg)

    def receive(self):
        packet = self.radio.receive(with_header=True)
        out = None
        if packet is not None:
            header = [hex(x) for x in packet[0:4]]
            payload = packet[4:]
            rssi = self.radio.last_rssi
            out = {"header": header, "payload": payload, "rssi": rssi}
        return out

    def poll(self):
        pass
