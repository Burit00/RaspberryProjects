from RPi import GPIO

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
LCD_WIDTH = 16
LCD_rows = 2
LCD_CHR = True
LCD_CMD = False

LCD_LINE_1 = 0x80
LCD_LINE_2 = 0xC0

# Define GPIO to LCD mapping
LCD_RS = 26
LCD_E = 16
LCD_D4 = 13
LCD_D5 = 6
LCD_D6 = 5
LCD_D7 = 12
LCD_ON = 15

# Timing constants
E_PULSE = 0.00005
E_DELAY = 0.00005


def lcd_init():
    GPIO.setmode(GPIO.BCM)          # Use BCM GPIO numbers
    GPIO.setup(LCD_E, GPIO.OUT)     # E
    GPIO.setup(LCD_RS, GPIO.OUT)    # RS
    GPIO.setup(LCD_D4, GPIO.OUT)    # D4
    GPIO.setup(LCD_D5, GPIO.OUT)    # D5
    GPIO.setup(LCD_D6, GPIO.OUT)    # D6
    GPIO.setup(LCD_D7, GPIO.OUT)    # D7
    GPIO.setup(LCD_ON, GPIO.OUT)    # Backlight enable

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

    GPIO.output(LCD_RS, mode)

    GPIO.output(LCD_D4, False)
    GPIO.output(LCD_D5, False)
    GPIO.output(LCD_D6, False)
    GPIO.output(LCD_D7, False)

    if bits & 0x10 == 0x10:
        GPIO.output(LCD_D4, True)
        GPIO.output(LCD_D5, True)
        GPIO.output(LCD_D6, True)
        GPIO.output(LCD_D7, True)
