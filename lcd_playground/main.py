from RPLCD import CharLCD

# 1 : GND
# 2 : 5V
# 3 : Contrast(0-5V)*
# 4 : RS (Register Select)
# 5 : R/W (Read / Write)    -GROUND this PIN
# 6 : Enable or Strobe
# 7 : Data bit 0            -NOT USED
# 8 : Data bit 1            -NOT USED
# 9 : Data bit 2            -NOT USED
# 10 : Data bit 3            -NOT USED
# 11: Data bit 4
# 12: Data bit 5
# 13: Data bit 6
# 14: Data bit 7
# 15: LCD Backlight +5V**
# 16: LCD Backlight GND

lcd = CharLCD(cols=16, rows=2, pin_rs=26, pin_e=19, pins_data=[13, 6, 5, 7])
lcd.write_string("Hello World!")
