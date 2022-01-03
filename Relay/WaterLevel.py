import RPi.GPIO as GPIO
import time

pin1 = 36 # set pin
GPIO.setmode(GPIO.BCM)

class WLVL:
    
    def Read(self):
        GPIO.setup(pin1, GPIO.OUT)
        a = GPIO.output(pin1, True)
        print(a)
        GPIO.output(pin1, False)
        
        
x = WLVL()
x.Read()
        