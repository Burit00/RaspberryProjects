import gpiozero
from time import sleep

led = gpiozero.LED(14)


def loop():
    while(True):
        led.on()
        sleep(1)
        led.off()
        sleep(1)


if __name__ == "__main__":
    #setup()
    loop()

