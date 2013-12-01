#!/usr/bin/python

import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

#Pin assignments

#Motors (Clockwise assignment)
#FRONT
#RIGHT
#BACK
#LEFT

#Gyro pin
#Accel pin

#Global Variables
#max pwm prop speed
#min pwm prop speed

def pwm_example():
    #PWM Example: https://code.google.com/p/raspberry-gpio-python/wiki/PWM
    GPIO.setup(12,GPIO.OUT)
    p = GPIO.PWM(12, 50) #Channel 12, frequency 50
    p.start(1)
    raw_input('Press return to stop:')
    p.stop()
    GPIO.cleanup()

def main():
    print("Here we go!")
    #Startup and setup
    #Setup pins
    #Set up PWM
    #Accel Setup
    #Gyro Setup

if __name__ == "__main__":
    main()

