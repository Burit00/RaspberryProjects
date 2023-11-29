import adafruit_dht


def init_dht(pin: int):
    dht_pin = adafruit_dht.Pin(pin)
    return adafruit_dht.DHT22(dht_pin)
