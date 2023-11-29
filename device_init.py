import gpiozero

from BMP280 import BMP280 as BMP280Sensor
from DHT.DHT import init_dht
from board_setup import *
from LCD.LCD import LCD as LCDScreen

# Sensors
LCD = LCDScreen(rs=LCD_RS, en=LCD_E, d4=LCD_D4, d5=LCD_D5, d6=LCD_D6, d7=LCD_D7, cols=LCD_COLS, rows=LCD_ROWS)
DHT = init_dht(DHT_PIN)
BMP280 = BMP280Sensor.bmp280

# Buttons
CEL_FAHR_BTN = gpiozero.Button(CELSIUS_FAHRENHEIT_SWITCH_BUTTON)

# Buzzers
HIGH_HUMIDITY_BUZZ = gpiozero.TonalBuzzer(HIGH_HUMIDITY_BUZZER)
