import RPi.GPIO as GPIO
from time import sleep
from random import randint

GPIO.setmode(GPIO.BCM)

#LED

d1 = 14
d2 = 15
d3 = 18
d4 = 23
d5 = 24
d6 = 25

#Button
button = 21

GPIO.setup(button,GPIO.IN, pull_up_down = GPIO.PUD_UP)

GPIO.setup(d1,GPIO.OUT)
GPIO.setup(d2,GPIO.OUT)
GPIO.setup(d3,GPIO.OUT)
GPIO.setup(d4,GPIO.OUT)
GPIO.setup(d5,GPIO.OUT)
GPIO.setup(d6,GPIO.OUT)

#Function to roll dice
def dice():
    for i in range(5):
        roll = randint(1,6)
    print(roll)
#Let's add some razzle dazzle!!
    for i in range(3):
        GPIO.output(d1,1)
        GPIO.output(d2,1)
        GPIO.output(d3,1)
        GPIO.output(d4,1)
        GPIO.output(d5,1)
        GPIO.output(d6,1)
        sleep(0.05)
        GPIO.output(d1,0)
        GPIO.output(d2,1)
        GPIO.output(d3,0)
        GPIO.output(d4,1)
        GPIO.output(d5,0)
        GPIO.output(d6,1)
        sleep(0.05)
        GPIO.output(d1,1)
        GPIO.output(d2,0)
        GPIO.output(d3,1)
        GPIO.output(d4,0)
        GPIO.output(d5,1)
        GPIO.output(d6,0)
        sleep(0.05)
        GPIO.output(d1,0)
        GPIO.output(d2,0)
        GPIO.output(d3,0)
        GPIO.output(d4,0)
        GPIO.output(d5,0)
        GPIO.output(d6,0)
        sleep(0.05)
    if roll == 1:
            GPIO.output(d1,1)
            sleep(3)
            GPIO.output(d1,0)
    elif roll == 2:
            GPIO.output(d1,1)
            GPIO.output(d2,1)
            sleep(3)
            GPIO.output(d1,0)
            GPIO.output(d2,0)
    elif roll == 3:
            GPIO.output(d1,1)
            GPIO.output(d2,1)
            GPIO.output(d3,1)
            sleep(3)
            GPIO.output(d1,0)
            GPIO.output(d2,0)
            GPIO.output(d3,0)	
    elif roll == 4:	
            GPIO.output(d1,1)
            GPIO.output(d2,1)
            GPIO.output(d3,1)
            GPIO.output(d4,1)
            sleep(3)
            GPIO.output(d1,0)
            GPIO.output(d2,0)
            GPIO.output(d3,0)
            GPIO.output(d4,0)	
    elif roll == 5:	
            GPIO.output(d1,1)
            GPIO.output(d2,1)
            GPIO.output(d3,1)
            GPIO.output(d4,1)
            GPIO.output(d5,1)
            sleep(3)
            GPIO.output(d1,0)
            GPIO.output(d2,0)
            GPIO.output(d3,0)
            GPIO.output(d4,0)	
            GPIO.output(d5,0)
    elif roll == 6:	
            GPIO.output(d1,1)
            GPIO.output(d2,1)
            GPIO.output(d3,1)
            GPIO.output(d4,1)
            GPIO.output(d5,1)
            GPIO.output(d6,1)
            sleep(3)
            GPIO.output(d1,0)
            GPIO.output(d2,0)
            GPIO.output(d3,0)
            GPIO.output(d4,0)	
            GPIO.output(d5,0)
            GPIO.output(d6,0)

while True:
    if GPIO.input(button) == False:
        dice()
