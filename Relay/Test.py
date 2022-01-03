import RPi.GPIO as GPIO
import time

pin1 = 23 # 23
pin2 = 26 # 26

which = 2
sec = 3

GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin1, GPIO.OUT)
#GPIO.output(pin1, False)
GPIO.setup(pin2, GPIO.OUT)
#GPIO.output(pin2, False)
try:
    if (which == 1):
        GPIO.output(pin1, GPIO.HIGH)
        time.sleep(sec)
        GPIO.output(pin1, GPIO.LOW)
    elif (which == 2):
        GPIO.output(pin2, GPIO.HIGH)
        time.sleep(sec)
        GPIO.output(pin2, GPIO.LOW)
    GPIO.cleanup()
except:
    pass