import RPi.GPIO as GPIO
import time
#from gpiozero import OutputDevice

pin1 = 23
pin2 = 26

class Relay():
        
    def Work(self, which, sec):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin1, GPIO.OUT)
        GPIO.output(pin1, False)
        GPIO.setup(pin2, GPIO.OUT)
        GPIO.output(pin2, False)
        try :
            if (which == 1):
                GPIO.output(pin1, True)
                time.sleep(sec)
                GPIO.output(pin1, False)
            elif (which == 2):
                GPIO.output(pin2, True)
                time.sleep(sec)
                GPIO.output(pin2, False)
        except KeyboardInterrupt:
            GPIO.cleanup()
            
        
s = Relay()
s.Work(2, 480)

