import lcd
from time import sleep

lcd.lcd_init()
while True:
    sleep(1)
    lcd.lcd_string("Raspberry Pi")
    sleep(1)
    lcd.lcd_string("")

