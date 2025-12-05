from ota import ota_update
from machine import Pin
import time


ota_update()   # check update
print("Running main app...")



led = Pin(2, Pin.OUT)

while True:
    led.value(1)   # LED ON
    time.sleep(2)
    led.value(0)   # LED OFF
    time.sleep(2)
