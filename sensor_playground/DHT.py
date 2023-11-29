import adafruit_dht

DHT_PIN = adafruit_dht.Pin(4)
dht = adafruit_dht.DHT22(DHT_PIN)
