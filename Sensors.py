

from machine import Pin
import time

trig = Pin(4, Pin.OUT)
echo = Pin (5, Pin.IN, Pin.PULL_DOWN)

# 5 and 6 Pins for other sensor

while True:
    
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
    print (round(distance, 1), "cm")