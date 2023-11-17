import lcd
from time import sleep

while True:
    lcd.lcd_init()
    sleep(1)
    lcd.lcd_string("Raspberry Pi")
    sleep(1)

