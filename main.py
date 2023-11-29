import time
import signal
import operator
import asyncio
from datetime import datetime
import RPi.GPIO as GPIO

from device_init import *

GPIO.setwarnings(False)

is_celsius_mode = True
DEGREE_CHAR = chr(0xDF)


def switch_celsius_and_fahrenheit_mode():
    global is_celsius_mode
    is_celsius_mode = operator.not_(is_celsius_mode)


CEL_FAHR_BTN.when_activated = switch_celsius_and_fahrenheit_mode


def format_temperature(temperature: float):
    if is_celsius_mode:
        return f'{"{:4.1f}".format(temperature)}{DEGREE_CHAR}C'

    return f'{"{:4.1f}".format((temperature * 9 / 5) + 32)}{DEGREE_CHAR}F'


class GracefulKiller:
    kill_now = False

    def __init__(self):
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)

    def exit_gracefully(self, *args):
        self.kill_now = True


async def main():
    while not killer.kill_now:

        try:
            temperature = DHT.temperature
            humidity = DHT.humidity
            pressure = BMP280.pressure

            temperature_string = format_temperature(temperature)
            humidity_string = f"{'{:4.1f}'.format(humidity)}%"
            pressure_string = f"{int(pressure)}hPa"

            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            msg1 = LCD.space_between_just(temperature_string, humidity_string)[0]
            msg2 = LCD.space_between_just(pressure_string, current_time)[0]

            LCD.print(f"{msg1}\n{msg2}")
            time.sleep(0.2)
        except Exception as e:
            print(e)
            continue
    LCD.__del__()
    HIGH_HUMIDITY_BUZZ.stop()


if __name__ == '__main__':
    killer = GracefulKiller()
    asyncio.run(main())
