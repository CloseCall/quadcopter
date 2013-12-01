#!/usr/bin/python

import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

##Pin assignments
#Motors (Clockwise assignment)
FRONT_PIN=12
RIGHT_PIN=12
BACK_PIN=12
LEFT_PIN=12

#Gyroscope
GYRO_PIN=13
#Accelerometer
ACCEL_PIN=13

##Pin setup
GPIO.setup(FRONT_PIN,GPIO.OUT)
GPIO.setup(RIGHT_PIN,GPIO.OUT)
GPIO.setup(BACK_PIN,GPIO.OUT)
GPIO.setup(LEFT_PIN,GPIO.OUT)       
GPIO.setup(GYRO_PIN,GPIO.IN)       
GPIO.setup(ACCEL_PIN,GPIO.IN)


##Global Variables

#PWD Speed table
SPEED_MIN, SPEED_0 = 0,0
SPEED_1=0
SPEED_2=0
SPEED_3=0
SPEED_4=0
SPEED_5=0
SPEED_6=0
SPEED_7=0
SPEED_8=0
SPEED_9=0
SPEED_MAX, SPEED_10 = 0,0

#Duty Cycle
#Dependant on ESC
FREQUENCY=50
#ESCs recieve at 50hz, but usually average 5-10. 490 will override this
#FREQUENCY=490

#Initialize PWM variables
FRONT = GPIO.PWM(FRONT_PIN, FREQUENCY)
RIGHT = GPIO.PWM(RIGHT_PIN, FREQUENCY)
BACK = GPIO.PWM(BACK_PIN, FREQUENCY)
LEFT = GPIO.PWM(LEFT_PIN, FREQUENCY)

def pwm_example():
    #PWM Example: https://code.google.com/p/raspberry-gpio-python/wiki/PWM
    GPIO.setup(12,GPIO.OUT)
    p = GPIO.PWM(12, 50) #Channel 12, frequency 50
    p.start(1)
    raw_input('Press return to stop:')
    p.stop()
    GPIO.cleanup()

def pwm_example2():
    from RPIO import PWM

    # Setup PWM and DMA channel 0
    PWM.setup()
    PWM.init_channel(0)
    
    # Add some pulses to the subcycle
    PWM.add_channel_pulse(0, 17, 0, 50)
    PWM.add_channel_pulse(0, 17, 100, 50)
    
    # Stop PWM for specific GPIO on channel 0
    PWM.clear_channel_gpio(0, 17)
    
    # Shutdown all PWM and DMA activity
    PWM.cleanup()

def main():
    print("Here we go!")
    ##Startup and setup

    #prop start
    FRONT.start(SPEED_MIN)
    RIGHT.start(SPEED_MIN)
    BACK.start(SPEED_MIN)
    LEFT.start(SPEED_MIN)


    #Set up PWM
    #Accel Setup
    #Gyro Setup
    

    GPIO.cleanup() #If it actually exits, we need to clean it all up


#Directional functions

#Stay in place
def hover(time=0, speed=SPEED_MAX):
    #stub
    return

def forward(speed):
    #stub
    return

def turn(direction):
    #stub
    return

def up(speed):
    #stub
    return

def down(speed):
    #stub
    return

def left(speed):
    #stub
    return

def right(speed):
    #stub
    return

def back(speed):
    #stub
    return

#Set motor and speed... do I really need this function?? Fill in for now
def motor_control(motor, speed):
    motor.ChangeDutyCycle(speed)

#Quad test. All the basic functions of the quad
#Test should go as follows:
#Move up, back down, turn 180, forward, back, side left, side right
#Maybe add a flip or something
def test_mod():
    print("test stub")

if __name__ == "__main__":
    main()

