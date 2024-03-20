from machine import Pin
import time

stepDivision = 0.25
stepsPerDegree = (200 / stepDivision) / 360

direction1 = Pin(14, Pin.OUT)
step1 = Pin(15, Pin.OUT)

direction2 = Pin(16, Pin.OUT)
step2 = Pin(17, Pin.OUT)

def move(deg1, deg2):
    if deg1 < 0:
        direction1.on()
        deg1 = abs(deg1)
    else:
        direction1.off()
        
    if deg2 < 0:
        direction2.on()
        deg2 = abs(deg2)
    else:
        direction2.off()
        
    noSteps1 = deg1 * (200 / 0.25) / 360
    noSteps2 = deg2 * (200 / 0.25) / 360
    
    for i in range(max(noSteps1, noSteps2) * stepsPerDegree):
        
        if i < noSteps1: step1.on()
        if i < noSteps2: step2.on()
        time.sleep(0.005)
        if i < noSteps1: step1.off()
        if i < noSteps2: step2.off()
        time.sleep(0.005)
# (from front) left (pos turns clock) right (clock)
move(-10, 10) # draw edge 1
time.sleep(0.5)
move(5, -5) # draw edge 2
time.sleep(0.5)
move(-0, -5) # draw edge 3
time.sleep(0.5)
move(5, -5) # draw edge 4