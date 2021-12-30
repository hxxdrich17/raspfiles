import ModuleDHT11
import configparser
import time

class Checks:

    def Check_DHT(self, stat=False):
        global min_temp, max_temp, min_humid
        #time.sleep(60)
        dht = ModuleDHT11.DHT()
        #print(dht.Data()[1], type(dht.Data()[1]))
        #temp = dht.Data()[0]
        #humid = dht.Data()[1]
        try:
            temp = dht.Data()[0]
        except:
            temp = 0
        try:
            humid = dht.Data()[1]
            #print(humid)
        except:
            humid = 0

        if (humid < min_humid and humid != 0):
            return "humid", humid
        
        #if (temp < min_temp and temp != 0):
        #    return "min_temp", temp

        if (temp > max_temp and temp != 0):
            return "max_temp", temp
        
        if (temp == 0 or humid == 0):
            return "", 0
        
        if (stat == True):
            return temp, humid

    def Normalized(self, name, num):
        global min_temp, max_temp, min_humid
        dht = ModuleDHT11.DHT()
        temp = dht.Data()[0]
        humid = dht.Data()[1]
        # TODO: depends on water level, not humidity (done)

        if (name == "max_temp"):
            if (temp < num and temp < max_temp):
                return True
            elif (temp >= num and temp >= max_temp):
                return False

    def __init__(self):
        global min_temp, max_temp, min_humid
        config = configparser.RawConfigParser()
        config.read("/home/pi/Desktop/Hydro/Settings/Config.conf")  # TODO: Linux path
        #min_temp = config.getint("cfg", "Minimum_temperature")
        #max_temp = config.getint("cfg", "Maximum_temperature")
        #min_humid = config.getint("cfg", "Minimum_humidity")
        min_temp = 28
        max_temp = 34
        min_humid = 80
        
#ck = Checks()
#print(ck.Check_DHT())
