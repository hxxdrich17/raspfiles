# pip install dht11
import RPi.GPIO as GPIO
import dht11

class DHT:

	def Data(self):
		GPIO.setwarnings(True)
		GPIO.setmode(GPIO.BCM) # initialize GPIO

		instance = dht11.DHT11(pin=24) # read data using pin 14

		try:
			result = instance.read()
			if (result.is_valid()):
				temperature = result.temperature
				humidity = result.humidity
				return [float(temperature), float(humidity)]

		except KeyboardInterrupt:
			print("Cleanup")
			GPIO.cleanup()
			
#start = DHT()
#print(start.Data())
