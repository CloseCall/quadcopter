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

#NOTE: Pins for Sensors will probably change... will most likely be using I2C
#Gyroscope
GYROX_PIN=13
GYROY_PIN=13
GYROZ_PIN=13
GYRO_TOLERANCE=0 #Sensors aren't perfect...

#Accelerometer
ACCELX_PIN=13
ACCELY_PIN=13
ACCELZ_PIN=13
ACCEL_TOLERANCE=0
#Altimeter
BAR_PIN=1

##Pin setup
GPIO.setup(FRONT_PIN,GPIO.OUT)
GPIO.setup(RIGHT_PIN,GPIO.OUT)
GPIO.setup(BACK_PIN,GPIO.OUT)
GPIO.setup(LEFT_PIN,GPIO.OUT)       
#TODO: Setup gyro, accel, alti, etc.


##Global Variables

#PWD Speed table, unsure if it's necessary but it's here for now
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
    
    #Command List

    #Loop forever, going through command list.

    GPIO.cleanup() #If it actually exits, we need to clean it all up
    
    #Maybe shutdown

#Directional functions

#Stay in place
#Time or distance TBD
def hover(time=0, speed=SPEED_MAX):
    #Need Altimeter data
    #save alti data
    #Loop:
    #If within tolerance, need to go up and down
    #If above or below, should adjust speed according to distance
    return

#Back top speed, left+right middle speed, front low speed. 
#Eventually tilt until fully vertical and maintain? 
#Or keep 45 degrees?
#Same goes for other strafe movements
def forward(speed):
    #stub
    return

#To turn, left and right top speed, bottom and top low speed
#Remember to maintain height!
def turn(direction):
    #stub
    return

#All fans up? Stabilize as you go up?
def up(speed):
    #Loop:
    #Stabilize
    #All fans up
    #Check gyro data
    #Correct fan speeds
    #Check time
    #Rinse and repeat
    return

#Lower fan speeds?
def down(speed):
    #stub
    return

#Right top speed, front and back mid speed, left low speed
def left(speed):
    #stub
    return

#Left top speed, front and back mid speed, right low speed
def right(speed):
    #stub
    return

#Front top speed, left right middle speed, back low speed
def back(speed):
    #stub
    return

def stabilize():
    #Loop:
    #read gyro data
    #Calc diff between horizontal and data
    #within tolerance?
    #If not, adjust for X and Y axis    
    #Else return

    return

#set all motor speeds
def motor_speed(front, right, back, left):
    #Don't change speeds if 0!
    if front != 0:
        FRONT.ChangeDutyCycle(front)
    if right != 0:
        RIGHT.ChangeDutyCycle(right)
    if back != 0:
        BACK.ChangeDutyCycle(back)
    if left != 0:
        LEFT.ChangeDutyCycle(left)

#Read pin data (accel or gyro)
def get_sensor(pin):
    data=0
    #stub
    return data

#Quad test. All the basic functions of the quad
#Test should go as follows:
#Move up, back down, turn 180, forward, back, side left, side right
#Maybe add a flip or something
def test_mod():
    print("test stub")

if __name__ == "__main__":
    main()

