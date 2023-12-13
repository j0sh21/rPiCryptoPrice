#!/usr/bin/env python3
########################################################################
# Filename    : Blink.py
# Description : Basic usage of GPIO. Let led blink.
# auther      : www.freenove.com
# Customizig by: j0sh21
# modification: 2019/12/28
########################################################################
import RPi.GPIO as GPIO
import mariadb
import config

ledPin = 11
ledgreen = 16
led24r = 13
led24g = 36
led7g = 38
led7r = 31
volday = 33

lastred = 18
lastgreen = 22

def setup():
    GPIO.setmode(GPIO.BOARD)       # use PHYSICAL GPIO Numbering
    GPIO.setup(ledPin, GPIO.OUT)   # set the ledPin to OUTPUT mode
    GPIO.output(ledPin, GPIO.LOW)  # make ledPin output LOW level
    GPIO.setup(ledgreen, GPIO.OUT)   # set the ledPin to OUTPUT mode
    GPIO.output(ledgreen, GPIO.LOW)
    GPIO.setup(led24r, GPIO.OUT)   # set the ledPin to OUTPUT mode
    GPIO.output(led24r, GPIO.LOW)  # make ledPin output LOW level
    GPIO.setup(led24g, GPIO.OUT)   # set the ledPin to OUTPUT mode
    GPIO.output(led24g, GPIO.LOW)
    GPIO.setup(led7r, GPIO.OUT)   # set the ledPin to OUTPUT mode
    GPIO.output(led7r, GPIO.LOW)  # make ledPin output LOW level
    GPIO.setup(led7g, GPIO.OUT)   # set the ledPin to OUTPUT mode
    GPIO.output(led7g, GPIO.LOW)
    GPIO.setup(volday, GPIO.OUT)   # set the ledPin to OUTPUT mode
    GPIO.output(volday, GPIO.LOW)
    GPIO.setup(lastred, GPIO.OUT)   # set the ledPin to OUTPUT mode
    GPIO.output(lastred, GPIO.LOW)
    GPIO.setup(lastgreen, GPIO.OUT)   # set the ledPin to OUTPUT mode
    GPIO.output(lastgreen, GPIO.LOW)
    print ('using pin%d'%ledPin)

def loop():
    if 1 ==1:
    
        con = mariadb.connect(user=config.duser, password=config.dpassword, host=config.dhost, database=config.ddatabase)
        cur = con.cursor()
        e = f"select * from {config.conin2display} where fetch_id=(select max(fetch_id) from {config.conin2display});;"
        cur.execute(e)
        data = cur.fetchall()
        first_column = [row[0] for row in data]
        print(first_column)
        percent1hour = [row[4] for row in data]
        percent24hour = [row[5] for row in data]
        percent7day = [row[6] for row in data]
        pvolday = [row[3] for row in data]
        
        e=f"select * from {config.conin2display} where fetch_id=(select max(fetch_id)-1 from {config.conin2display});;"
        cur.execute(e)
        data_old = cur.fetchall()
        first_column_old = [row[0] for row in data_old]

        if not first_column_old:
            first_column_old = 0
        if not first_column:
            first_column = 0
        if first_column and first_column_old: 

            if float(str(first_column)[1:-1]) < float(str(first_column_old)[1:-1]):
                GPIO.output(lastred, GPIO.HIGH)
                GPIO.output(lastgreen, GPIO.LOW)
                print(str(first_column))
                print(str(first_column_old))
            else:
                GPIO.output(lastred, GPIO.LOW)
                GPIO.output(lastgreen, GPIO.HIGH)
                print(str(first_column))
                print(str(first_column_old))
        if percent1hour:
            if float(str(percent1hour)[1:-1]) < 0:
                GPIO.output(ledPin, GPIO.HIGH)
                GPIO.output(ledgreen, GPIO.LOW)# make ledPin output HIGH level to turn on led
                print ('led turned on >>>')     # print information on terminal
                                   # Wait for 1 second
            else:
                GPIO.output(ledgreen, GPIO.HIGH)
                GPIO.output(ledPin, GPIO.LOW)   # make ledPin output LOW level to turn off led
                print ('led1 turned off <<<')
                                  # Wait for 1 second
                
        if percent24hour:
            if float(str(percent24hour)[1:-1]) < 0:
                GPIO.output(led24r, GPIO.HIGH)
                GPIO.output(led24g, GPIO.LOW)# make ledPin output HIGH level to turn on led
                print ('led turned on >>>')     # print information on terminal
                               # Wait for 1 second
            else:
                GPIO.output(led24g, GPIO.HIGH)
                GPIO.output(led24r, GPIO.LOW)   # make ledPin output LOW level to turn off led
                print ('led24 turned off <<<')
        if percent7day:
            if float(str(percent7day)[1:-1]) < 0:
                GPIO.output(led7r, GPIO.HIGH)
                GPIO.output(led7g, GPIO.LOW)# make ledPin output HIGH level to turn on led
                print ('led turned on >>>')     # print information on terminal
                               # Wait for 1 second
            else:
                GPIO.output(led7g, GPIO.HIGH)
                GPIO.output(led7r, GPIO.LOW)   # make ledPin output LOW level to turn off led
                print ('led24 turned off <<<')
            
        if pvolday:
            if float(str(pvolday)[1:-1]) > 0:
                GPIO.output(volday, GPIO.HIGH)
                # make ledPin output HIGH level to turn on led
                print ('volumen led turned on >>>')     # print information on terminal
                                   # Wait for 1 second
            else:
                GPIO.output(volday, GPIO.LOW)
                print ('volumen led turned off <<<')
                                  # Wait for 1 second
                       # Wait for 1 second
        
def destroy():
    GPIO.cleanup()                      # Release all GPIO

def main():
    print ('Program is starting ... \n')
    setup()
    try:
        loop()
    except KeyboardInterrupt:   # Press ctrl-c to end the program.
        destroy()

if __name__ == '__main__':
    main()
    

