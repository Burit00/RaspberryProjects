from board_pinout import *
from Adafruit_CharLCD import Adafruit_CharLCD

LCD_COLS = 16
LCD_ROWS = 2

lcd = Adafruit_CharLCD(rs=LCD_RS, en=LCD_E,
                       d4=LCD_D4, d5=LCD_D5, d6=LCD_D6, d7=LCD_D7,
                       cols=LCD_COLS, rows=LCD_ROWS
                       )
def main():
    lcd.clear()
    lcd.message("Chuj do dupy!")
