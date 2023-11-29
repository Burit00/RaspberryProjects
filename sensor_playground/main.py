from time import sleep

from DHT import dht
from BMP280 import bmp280

while True:
    sleep(2)
    print("xd")
    try:
        t1 = dht.temperature
        h = dht.humidity
        t2 = bmp280.temperature
        p = bmp280.pressure
        a = bmp280.altitude
        if t1 is not None and t2 is not None and h is not None and p is not None:
            print(f"Temperature1: {t1}°C, Humidity: {h}%, Pressure")
            print(f"Temperature2: {t2}°C, Pressure: {p} hPa, Altitude: {a}m")
        else:
            print("Failed to read data from one or more sensors.")
    except Exception as e:
        print(f"Error: {e}")
