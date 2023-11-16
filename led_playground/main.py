import gpiozero
from time import sleep

led_red = gpiozero.LED(14)
led_green = gpiozero.LED(15)


def loop():
    while True:
        led_red.on()
        led_green.off()
        sleep(1)
        led_red.off()
        led_green.on()
        sleep(1)


if __name__ == "__main__":
    #setup()
    loop()

