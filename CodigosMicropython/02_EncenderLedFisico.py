from machine import Pin
import time


led02=Pin(2, Pin.OUT)#D4


while True:
    
    led02.on()
    
    time.sleep_ms(2000)
    
    led02.off()
    
    time.sleep_ms(2000)
    
