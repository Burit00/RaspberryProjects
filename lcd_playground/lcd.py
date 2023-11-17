import RPi.GPIO as GPIO
import gpiozero
from time import sleep
from board_pinout import *

# 1 : GND
# 2 : 5V
# 3 : Contrast(0-5V)*
# 4 : RS (Register Select)
# 5 : R/W (Read / Write)    -GROUND this PIN
# 6 : Enable or Strobe
# 7 : Data bit 0            -NOT USED
# 8 : Data bit 1            -NOT USED
# 9 : Data bit 2            -NOT USED
# 10 : Data bit 3           -NOT USED
# 11: Data bit 4
# 12: Data bit 5
# 13: Data bit 6
# 14: Data bit 7
# 15: LCD Backlight +5V**
# 16: LCD Backlight GND

# Define device constants
RS = gpiozero.LED(LCD_RS)
E = gpiozero.LED(LCD_E)
D4 = gpiozero.LED(LCD_D4)
D5 = gpiozero.LED(LCD_D5)
D6 = gpiozero.LED(LCD_D6)
D7 = gpiozero.LED(LCD_D7)

LCD_WIDTH = 16
LCD_rows = 2
LCD_CHR = True
LCD_CMD = False

LCD_LINE_1 = 0x80
LCD_LINE_2 = 0xC0


# Timing constants
E_PULSE = 0.005
E_DELAY = 0.005


def main():
    # Main program block


    # Initialise display
    lcd_init()

    # Send some centred test
    print(1)
    lcd_byte(LCD_LINE_1, LCD_CMD)
    lcd_string("Rasbperry Pi", 2)
    lcd_byte(LCD_LINE_2, LCD_CMD)
    lcd_string("Model B", 2)

    sleep(3)  # 3 second delay

    # Send some left justified text
    print(2)
    lcd_byte(LCD_LINE_1, LCD_CMD)
    lcd_string("1234567890123456", 1)
    lcd_byte(LCD_LINE_2, LCD_CMD)
    lcd_string("abcdefghijklmnop", 1)

    sleep(3)  # 3 second delay

    # Send some right justified text
    print(3)
    lcd_byte(LCD_LINE_1, LCD_CMD)
    lcd_string("Raspberrypi-spy", 3)
    lcd_byte(LCD_LINE_2, LCD_CMD)
    lcd_string(".co.uk", 3)

    sleep(3)


def lcd_init():
    # GPIO.setmode(GPIO.BCM)  # Use BCM GPIO numbers
    # GPIO.setup(LCD_E, GPIO.OUT)  # E
    # GPIO.setup(LCD_RS, GPIO.OUT)  # RS
    # GPIO.setup(LCD_D4, GPIO.OUT)  # D4
    # GPIO.setup(LCD_D5, GPIO.OUT)  # D5
    # GPIO.setup(LCD_D6, GPIO.OUT)  # D6
    # GPIO.setup(LCD_D7, GPIO.OUT)  # D7

    lcd_byte(0x33, LCD_CMD)
    lcd_byte(0x32, LCD_CMD)
    lcd_byte(0x28, LCD_CMD)
    lcd_byte(0x0C, LCD_CMD)
    lcd_byte(0x06, LCD_CMD)
    lcd_byte(0x01, LCD_CMD)


def lcd_string(message, style=1):
    if style == 1:
        message = message.ljust(LCD_WIDTH, " ")
    elif style == 2:
        message = message.center(LCD_WIDTH, " ")
    if style == 3:
        message = message.rjust(LCD_WIDTH, " ")

    for i in range(LCD_WIDTH):
        lcd_byte(ord(message[i]), LCD_CHR)


def lcd_byte(bits, mode):
    # Send byte to data pins
    # bits = data
    # mode = True  for character
    #        False for command

    #GPIO.output(LCD_RS, mode)  # RS

    if mode:
        RS.on()
    else:
        RS.off()

    # High bits
    D4.off()
    # GPIO.output(LCD_D4, False)
    D5.off()
    # GPIO.output(LCD_D5, False)
    D6.off()
#     GPIO.output(LCD_D6, False)
    D7.off()
#     GPIO.output(LCD_D7, False)
    if bits & 0x10 == 0x10:
        D4.on()
        # GPIO.output(LCD_D4, True)
    if bits & 0x20 == 0x20:
        D5.on()
        # GPIO.output(LCD_D5, True)
    if bits & 0x40 == 0x40:
        D6.on()
        # GPIO.output(LCD_D6, True)
    if bits & 0x80 == 0x80:
        D7.on()
        # GPIO.output(LCD_D7, True)

    # Toggle 'Enable' pin
    sleep(E_DELAY)
    E.on()
    #GPIO.output(LCD_E, True)
    sleep(E_PULSE)
    E.off()
    #GPIO.output(LCD_E, False)
    sleep(E_DELAY)

    # Low bits
    D4.off()
    # GPIO.output(LCD_D4, False)
    D5.off()
    # GPIO.output(LCD_D5, False)
    D6.off()
#     GPIO.output(LCD_D6, False)
    D7.off()
#     GPIO.output(LCD_D7, False)
    if bits & 0x01 == 0x01:
        D4.on()
        GPIO.output(LCD_D4, True)
    if bits & 0x02 == 0x02:
        D5.on()
        GPIO.output(LCD_D5, True)
    if bits & 0x04 == 0x04:
        D6.on()
        GPIO.output(LCD_D6, True)
    if bits & 0x08 == 0x08:
        D7.on()
        GPIO.output(LCD_D7, True)

    # Toggle 'Enable' pin
    sleep(E_DELAY)
    E.on()
    #GPIO.output(LCD_E, True)
    sleep(E_PULSE)
    E.off()
    #GPIO.output(LCD_E, False)
    sleep(E_DELAY)
