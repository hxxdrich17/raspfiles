from Relay import Setup
import ModuleDHT11
from Relay import Check
import datetime
import time
import configparser

config = configparser.RawConfigParser()
config.read("/home/pi/Desktop/Hydro/Settings/Config.conf")  # TODO: Linux path
# sec = config.getint("conf", "Seconds_for_filling")
sec = 10
rel = Setup.Relay()
ck = Check.Checks()

class Relay:

    def Logs(self, id, num="-"):
        date = str(datetime.datetime.now().strftime("%d.%m.%y %H:%M:%S"))
        f = open("Logs/Logs.txt", "a", encoding="UTF-8")
        if (id == 1):
            f.write(f"[{date}] Заливка воды {sec} секунд. Причина: {num}% влажности.")
        if (id == 2):
            f.write(f"[{date}] Включение кулера для охлаждения. Причина: температура {num}°C.")
        f.close()

    def WaterPlant(self, relay, num):
        # TODO: id of relay (done)
        rel.Work(relay, sec)
        Relay.Logs(1, num)

    def Cooler(self, relay, num):
        #while (ck.Normalized("max_temp", num) == False):
        #    pass
        rel.Work(relay, sec)
        Relay.Logs(2, num)

    def Main(self):
        #time.sleep(10)
        check, num = ck.Check_DHT()
        #print(check, num)
        print(check, num)
        if (check != "" and num != 0):
            if (check == "humid"):
                print("humid")
                Relay.WaterPlant(1, 1, num)
            if (check == "max_temp"):
                print("max_temp")
                Relay.Cooler(1, 2, num)
        # TODO: Temperature and level of water (done)

    def __init__(self):
        while True:
            time.sleep(5)
            #print(1111)
            Relay.Main(1)
            
start = Relay()
