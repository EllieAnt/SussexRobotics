from machine import Pin
import time

trigger_x = Pin(0, Pin.OUT)
echo_x = Pin(1, Pin.IN, Pin.PULL_DOWN)

trigger_y = Pin(4, Pin.OUT)
echo_y = Pin(5, Pin.IN, Pin.PULL_DOWN)

stepDivision = 0.25
stepsPerDegree = (200 / stepDivision) / 360

direction1 = Pin(14, Pin.OUT)
step1 = Pin(15, Pin.OUT)

direction2 = Pin(16, Pin.OUT)
step2 = Pin(17, Pin.OUT)

base_distance_x = 0
base_distance_y = 0
max_distance_x = 0
max_distance_y = 0
min_distance_x = 0
min_distance_y = 0

#TODO: Create a min_x, min_y, max_x and max_y that determines the limits of how far the sensor should look. Also useful for showing speed

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

def get_real_distance_x(rounding = 1) -> float:
    trigger_x.on()
    time.sleep_us(2)
    trigger_x.off()
    
    while echo_x.value() == 0:
        start_time = time.ticks_us()
        
    while echo_x.value() == 1:
        end_time = time.ticks_us()
        
    distance = (end_time - start_time) / 58.8
    
    if rounding > 0:
        return round(distance, rounding)
    else:
        return distance


def get_real_distance_y(rounding = 1) -> float:
    trigger_y.on()
    time.sleep_us(2)
    trigger_y.off()
    
    while echo_y.value() == 0:
        start_time = time.ticks_us()
        
    while echo_y.value() == 1:
        end_time = time.ticks_us()
        
    distance = (end_time - start_time) / 58.8
    
    if rounding > 0:
        return round(distance, rounding)
    else:
        return distance

def get_relative_distance_x(rounding = 1) -> float:        
    distance = get_real_distance_x(0)
    
    if rounding > 0:
        return round(distance - base_distance_x, rounding)
    else:
        return distance - base_distance_x


def get_relative_distance_y(rounding = 1) -> float:
    distance = get_real_distance_y(0)
    
    if rounding > 0:
        return round(distance - base_distance_y, rounding)
    else:
        return distance - base_distance_y


def calibrate_sensors():
    # Stabilise sensors
    trigger_x.off()
    trigger_y.off()
    time.sleep(0.2)
    
    #Calculate the base distance for each sensor
    print('Calculating neutral for sensor X. Please keep your hand still...')
    
    base_distance_x = get_real_distance_x()
    
    for i in range(2, 7):
        base_distance_x += get_real_distance_x()
        base_distance_x / i
        
    print('Sensor X calibrated.')
    time.sleep(1)
    
    print('Calculating neutral for sensor Y. Please keep your hand still...')
    
    base_distance_y = get_real_distance_y()
    
    for i in range(2, 7):
        base_distance_y += get_real_distance_y()
        base_distance_y / i
        
    print('Sensor Y calibrated.')
    time.sleep(1)
    print('Calibration complete.')
    print(f'Neutral X: {base_distance_x}cm')
    print(f'Neutral Y: {base_distance_y}cm')
    print(f'Max X: {max_distance_x}cm')
    print(f'Max Y: {max_distance_y}cm')
    print(f'Min X: {min_distance_x}cm')
    print(f'Min Y: {min_distance_y}cm')


calibrate_sensors()
    