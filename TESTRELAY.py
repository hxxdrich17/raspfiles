from gpiozero import OutputDevice
import time

def __init__(self, pin, active_high):
    super(Relay, self).__init__(pin, active_high)


RELAY = Relay(12, False)  # TODO: Single pump, not all (done)
RELAY1 = Relay(13, False)  # TODO: Initialize pin of cooler

RELAY.on()
time.sleep(10)
RELAY.off()
RELAY1.on()
time.sleep(10)
RELAY1.off()
