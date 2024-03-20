#Imports
from machine import Pin
import time

#Definitions
trig = Pin(4, Pin.OUT)
echo = Pin (5, Pin.IN, Pin.PULL_DOWN)

trig2 = Pin(0, Pin.OUT)
echo2 = Pin (1, Pin.IN, Pin.PULL_DOWN)

stepDivision = 0.125 #to make motors smoother, make this smaller: pick a value from 1/2, 1/4, 1/8, 1/16. currently 1/8
stepsPerDegree = (200 / stepDivision) / 360 #how many steps to take per degree of movement.
    
direction1 = Pin(14, Pin.OUT)
step1 = Pin(15, Pin.OUT)

direction2 = Pin(16, Pin.OUT)
step2 = Pin(17, Pin.OUT)


#Function
def move(deg1, deg2):
    if deg1 < 0:
        direction1.on() #goes one direction
        deg1 = abs(deg1)#needs to be positive now for it to work.
    else:
        direction1.off() #goes another direction
        
    if deg2 < 0: #same but for other motor
        direction2.on()
        deg2 = abs(deg2)
    else:
        direction2.off()
        
    noSteps1 = deg1 * stepsPerDegree
    noSteps2 = deg2 * stepsPerDegree
    
    print(max(noSteps1, noSteps2) * stepsPerDegree,"\n")
    for i in range(max(noSteps1, noSteps2) * stepsPerDegree):
        
        if i < noSteps1: step1.on()
        if i < noSteps2: step2.on()
        time.sleep(0.005)
        if i < noSteps1: step1.off()
        if i < noSteps2: step2.off()
        time.sleep(0.005)
        
        
#Code

while True: #Runs forever.
    
    trig.off()
    time.sleep(0.1)
    
    trig.on()
    time.sleep_us(2)
    trig.off()
    
    while echo.value() == 0:
        start = time.ticks_us()
        
    while echo.value() == 1:
        end = time.ticks_us()
        
    distance = (end - start) / 58.8
    print (round(distance, 1), "D1")
######################################################    
    trig2.off()
    time.sleep(0.1)
    
    trig2.on()
    time.sleep_us(2)
    trig2.off()
    
    while echo2.value() == 0:
        start2 = time.ticks_us()
        
    while echo2.value() == 1:
        end2 = time.ticks_us()
        
    distance2 = (end2 - start2) / 58.8
    print (round(distance2, 1), "D2")
    
    #If we need a set value for distances.
    #distance = 0
    #distance2 = 5

    
    if distance < 10:
        print("D1 less than 10")
        distance = -abs(round(distance, 1))
        print(distance, "D1")
        
    if distance2 < 10:
        print("D2 less than 10")
        distance2 = -abs(round(distance2, 1))
        print(distance2, "D2")
        
        
    # If distance too large
    if distance > 20 or distance2 > 20:
        print("Not today thank you :)\n ")
        
    # Move
    else: 
        print("moving")
        move(distance, distance2)
    
    time.sleep(2)
    
############################################################################
    #when distance -ve turns right
    #when distance +ve turns left
    
