#!/usr/bin/env python3

# Filename    : I2CLCD1602.py
# Description : Use the LCD display data
# Author      : Base: freenove, Customizing: j0sh21

import RPi.GPIO as GPIO
from PCF8574 import PCF8574_GPIO
from Adafruit_LCD1602 import Adafruit_CharLCD
import mariadb
import config

buttonPin = 12    # define buttonPin

def setup():
    GPIO.setmode(GPIO.BOARD)        # use PHYSICAL GPIO Numbering
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # set buttonPin to PULL UP INPUT mode

def loop():
    i = 0
    count = 0
    while True:
        print(count)

        if GPIO.input(buttonPin)==GPIO.LOW: # if button is pressed
            i += 1
            if i == 1:
                count += 1
        else: # if button is relessed
            i = 0
 
def format_number(number, decimal_separator=",", thousand_separator="."):
    # Wandel die Nummer in einen String um, wobei das Dezimaltrennzeichen ein Punkt ist
    number_str = str(number)
    
    # Trennen die Teile vor und nach dem Dezimalpunkt
    parts = number_str.split(".")
    
    # Füge das Tausendertrennzeichen hinzu
    parts[0] = "{:,}".format(int(parts[0])).replace(",", thousand_separator)
    
    # Teile wieder zusammen fügen, wobei das Dezimaltrennzeichen verwendet wird
    number_str = decimal_separator.join(parts)
    
    return number_str



def loop():
    mcp.output(3,1)     # turn on LCD backlight
    lcd.begin(16,2)     # set number of LCD lines and columns
    i = 0
    count = 0
    if 1 == 1:
        con = mariadb.connect(user=config.duser, password=config.dpassword, host=config.dhost, database=config.ddatabase)
        cur = con.cursor()
        e = f"select * from {config.conin2display} where fetch_id=(select max(fetch_id) from {config.conin2display});"
        cur.execute(e)
        data = cur.fetchall()
        first_column = [row[0] for row in data]
        print(first_column)
        percent1hour = [row[4] for row in data]

        lcd.clear()
        lcd.setCursor(0,0)  # set cursor position
        lcd.message(f'{config.conin2display} : ' + format_number(float(str(first_column)[1:-1]))+' $\n')
        lcd.message(f'1H: {(str(percent1hour)[1:-1])} %')

def destroy():
    GPIO.cleanup() 
    lcd.clear()
    
PCF8574_address = 0x27  # I2C address of the PCF8574 chip.
PCF8574A_address = 0x3F  # I2C address of the PCF8574A chip.
# Create PCF8574 GPIO adapter.
try:
    mcp = PCF8574_GPIO(PCF8574_address)
except:
    try:
        mcp = PCF8574_GPIO(PCF8574A_address)
    except:
        print ('I2C Address Error !')
        exit(1)
# Create LCD, passing in MCP GPIO adapter.
lcd = Adafruit_CharLCD(pin_rs=0, pin_e=2, pins_db=[4,5,6,7], GPIO=mcp)

def main():
        print ('Program is starting ... ')
        setup()
        try:
            loop()
        except KeyboardInterrupt:
            destroy()

if __name__ == '__main__':
    main()
    

